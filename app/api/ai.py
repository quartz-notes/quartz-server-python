from typing import Any


from fastapi import APIRouter
import json
from app.services.ai import parse_model, summarize_model

router = APIRouter(prefix="/ai")


@router.post("/parse")
async def ai_parse(prompt: str):
    response = await parse_model.generate_content_async(prompt)
    return json.loads(response.text)


@router.post(path="/summarize")
async def ai_summarize(prompt: str) -> Any:
    response = await summarize_model.generate_content_async(
        "input: " + prompt + " summary: "
    )
    return response.text


@router.post(path="/tags")
async def ai_tags(prompt: str):
    return ["tag1", "tag2", "tag3"]
