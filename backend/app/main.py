from fastapi import FastAPI
from app.schemas import InternshipRequest
from app.groq_client import generate_ai_response
from app.prompt_templates import build_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="InternHub AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
def analyze_internship(data: InternshipRequest):
    prompt = build_prompt(data.student, data.internship_description)
    ai_output = generate_ai_response(prompt)
    return {"result": ai_output}
