from fastapi import APIRouter

from app.api.ai import router as ai_router
from app.api.users import router as users_router
from app.api.notes import router as notes_router

router = APIRouter(prefix="/api")


@router.get("/ping")
async def ping():
    return {"status": "morgen trek pososi"}
router.include_router(ai_router)
router.include_router(users_router)
router.include_router(notes_router)

















# async def summarize_note(note_text: str):
#     url = "http://localhost:11434/api/generate"
#     payload = {
#         "model": "llama3.2:1b",
#         "prompt": f"Summarize the following text accurately and concisely. Return plain text without any introductory phrases, explanations and comments. Respond like this: summary. Not use 'Here is a summary of the text in plain text', keep the meaning of the text and leave important points in it, Here text: {note_text}", #It might me markdown format, keep that in mind, but don't add anything from yourself. 
#         "stream": False,
#         "options": {
#             "num_keep": 5,
#             # "seed": 42,
#             # "num_predict": 100,
#             "top_k": 20,
#             "top_p": 0.9,
#             "min_p": 0.0,
#             "typical_p": 0.7,
#             "repeat_last_n": 33,
#             "temperature": 0.6,
#             "repeat_penalty": 1.4,
#             "presence_penalty": 1.2,
#             "frequency_penalty": 1.2,
#             "penalize_newline": True,
#             # "stop": ["\n", "user:"],
#             # "numa": False,
#             # "num_ctx": 1024,
#             # "num_batch": 2,
#             # "num_gpu": 1,
#             # "main_gpu": 0,
#             # "low_vram": False,
#             # "vocab_only": False,
#             # "use_mmap": True,
#             # "use_mlock": False,
#             # "num_thread": 8
#         }
#     }
#     headers = {"Content-Type": "application/json"}
    
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=payload, headers=headers) as response:
#             data = await response.json()
#             return data.get("response", "No response received").strip()

# # async def main():
# #     note = "The series depicts a conflict between Skibidi Toilets—singing human-headed toilets—and humanoids with CCTV cameras, speakers, and televisions in place of their heads. The Skibidi Toilets, led by G-Toilet, overtake humanity. Warfare soon develops between the toilets and the alliance of Cameramen, Speakermen, and TV-men. The Titan Cameraman and Titan Speakerman, strongest of their respective races, begin to turn the tide of war. But Scientist Toilet, the Skibidi Toilets' second-in-command and R&D chief, develops a mind control parasite that overtakes Titan Speakerman, causing him to turn on the alliance and cause mass carnage in their ranks. With the aid of Titan TV-man, Titan Speakerman is cured, and, as the fighting continues to escalate in a constant arms race, an alliance force strikes at the toilets' secret underground facility, killing Scientist Toilet. The force's sole survivor, Plungerman, learns that the facility and the enigmatic and omnipresent Secret Agent were somehow involved in the toilets' creation, but the Secret Agent kills him to protect the secret. "
# #     summary = await summarize_note(note)
# #     print(summary)

# # asyncio.run(main())

# @router.post("/ai")
# async def ai(prompt: str):
#     print(prompt)
#     res=await summarize_note(prompt)
#     return res
