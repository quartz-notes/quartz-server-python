from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.crud import get_current_user
from app.models import NoteDB, UserDB
from app.schemas import NoteCreate, NoteUpdate


router = APIRouter()


@router.post("/notes/")
async def create_note(
    note: NoteCreate,
    current_user: Annotated[UserDB, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    new_note = NoteDB(title=note.title, content=note.content, owner_id=current_user.id)
    db.add(new_note)
    await db.commit()
    return new_note


@router.get("/notes/")
async def get_user_notes(
    current_user: Annotated[UserDB, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(
        select(NoteDB.id).filter(NoteDB.owner_id == current_user.id)
    )
    notes = result.scalars().all()
    return {"notes": notes}


@router.put("/notes/{note_id}")
async def update_note(
    note_id: int,
    note_update: NoteUpdate,
    current_user: Annotated[UserDB, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(
        select(NoteDB).filter(NoteDB.id == note_id, NoteDB.owner_id == current_user.id)
    )
    note = result.scalars().first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    if note_update.title:
        note.title = note_update.title
    if note_update.content:
        note.content = note_update.content
    await db.commit()
    return note


@router.delete("/notes/{note_id}")
async def delete_note(
    note_id: int,
    current_user: Annotated[UserDB, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(
        select(NoteDB).filter(NoteDB.id == note_id, NoteDB.owner_id == current_user.id)
    )
    note = result.scalars().first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await db.delete(note)
    await db.commit()
    return {"detail": "Note deleted"}
