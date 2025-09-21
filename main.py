
from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Load the SpaCy medium English model for word vectors and NER
nlp = spacy.load("en_core_web_md")

# Initialize FastAPI application
app = FastAPI()

# Define the request body schema for similarity and entity routes
class TextRequest(BaseModel):
    text1: str = None
    text2: str = None
    text: str = None

# Root endpoint for testing server is up
@app.get("/")
def read_root():
    return {"message": "Welcome to the Word Embedding API built with FastAPI!"}

# Endpoint to calculate cosine similarity between two texts
@app.post("/similarity/")
def get_similarity(req: TextRequest):
    # Process both texts using SpaCy
    doc1 = nlp(req.text1)
    doc2 = nlp(req.text2)

    # Return similarity score (float)
    return {"similarity": doc1.similarity(doc2)}

# Endpoint to extract named entities from input text
@app.post("/entities/")
def get_entities(req: TextRequest):
    doc = nlp(req.text)

    # Return list of (entity text, entity label) pairs
    return {
        "entities": [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    }
