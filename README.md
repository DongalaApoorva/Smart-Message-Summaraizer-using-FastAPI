#  Smart Text Summarizer API (FastAPI + HuggingFace)

This project is a **FastAPI-based REST API** that uses the powerful [BART-large-CNN](https://huggingface.co/facebook/bart-large-cnn) model from HuggingFace Transformers to generate **abstractive summaries** from long input texts.

---

##  Features

-  Accepts plain text input
-  Generates concise summaries using a transformer-based model
-  FastAPI framework with automatic Swagger UI for testing
-  JSON-based request and response interface

---

##  Tech Stack

-  Python 3.10+
-  FastAPI
-  HuggingFace Transformers
-  BART-large-cnn model
-  Pydantic for validation
-  Uvicorn for serving

---

##  Installation

# Clone the repo
git clone https://github.com/your-username/text-summarizer-api.git
cd text-summarizer-api

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

## Running the App
uvicorn main:app --reload
Then visit: http://127.0.0.1:8000/docs

## Example Usage
POST /summarize

Request Body:
{
  "text": "Your long input paragraph goes here..."
}

Response:
{
  "summary": "Shortened version of the input text."
}
## Project Structure
smart-text-summarizer/
├── main.py                # FastAPI app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
## Contributing
Feel free to fork this repository, improve it, and open a pull request!

## What I Learned
Working with pre-trained NLP models using HuggingFace

Building RESTful APIs with FastAPI

Handling Pydantic validation and error management

Using Swagger UI for interactive API testing

