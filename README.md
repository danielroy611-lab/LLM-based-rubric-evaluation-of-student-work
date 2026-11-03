# LLM-based-rubric-evaluation-of-student-work
LLM-based rubric evaluation of student work, with structured outputs, retries, validation and an evaluation script. It runs in mock mode with no API key, and uses the Gemini free tier when you add a key.
# AI Rubric Feedback Evaluator
FastAPI service that scores a child's submission (e.g. public speaking transcript)
against a rubric using an LLM and returns structured, child-friendly feedback.

## Features
- Prompt design with rubric + safety rules (child-friendly, no personal data, prompt-injection guard)
- Structured JSON output validated with Pydantic
- Retries with exponential backoff, score clamping
- Evaluation script with a test dataset (`eval_runner.py`)
- Mock mode when no API key is set

## Run
pip install -r requirements.txt
uvicorn app:app --reload

## Future work
Compare multiple models on quality/latency/cost, add speech-to-text, RAG over rubrics.
