from typing import Annotated, Any


from fastapi import APIRouter, Depends
from pydantic import BaseModel
import json
from app.core.config import settings
from app.crud import get_current_user
from app.models import UserDB
from app.services.ai import parse_model, summarize_model

router = APIRouter(prefix="/ai")


class Request(BaseModel):
    prompt: str


@router.post("/parse")
async def ai_parse(current_user: Annotated[UserDB, Depends(get_current_user)],request: Request):
    response = await parse_model.generate_content_async(request.prompt)
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/summarize")
async def ai_summarize(current_user: Annotated[UserDB, Depends(get_current_user)],request: Request) -> Any:
    response = await summarize_model.generate_content_async(request.prompt)
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/tags")
async def ai_tags(current_user: Annotated[UserDB, Depends(get_current_user)],prompt: str):
    return ["tag1", "tag2", "tag3"]
