from typing import Any


from fastapi import APIRouter
from pydantic import BaseModel
import json
from app.services.ai import parse_model, summarize_model

router = APIRouter(prefix="/ai")


class Request(BaseModel):
    prompt: str


@router.post("/parse")
async def ai_parse(request: Request):
    response = await parse_model.generate_content_async(request.prompt)
    print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/summarize")
async def ai_summarize(request: Request) -> Any:
    response = await summarize_model.generate_content_async(request.prompt)
    print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/tags")
async def ai_tags(prompt: str):
    return ["tag1", "tag2", "tag3"]
