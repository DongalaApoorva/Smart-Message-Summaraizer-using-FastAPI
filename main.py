from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import torch
# Initialize FastAPI app
app = FastAPI(title="Text Summarization API")

# Load the BART summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Request schema
class SummarizationRequest(BaseModel):
    text: str

# Response schema
class SummarizationResponse(BaseModel):
    summary: str
@app.get("/")
def root():
    return {"message": "Welcome to the Text Summarization API!"}

@app.post("/summarize", response_model=SummarizationResponse)
def summarize_text(request: SummarizationRequest):
    input_text = request.text.strip()

    if not input_text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    # Truncate input to 1024 characters to fit model limits
    truncated = input_text[:1024]

    try:
        result = summarizer(truncated, max_length=100, min_length=25, do_sample=False)
        return {"summary": result[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {e}")
