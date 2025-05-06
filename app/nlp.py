import spacy
from datetime import datetime
from dateutil import parser
import re

nlp = spacy.load("en_core_web_sm")

def categorize_task(title: str, description: str) -> str:
    text = f"{title} {description}".lower()
    if "meeting" in text or "schedule" in text:
        return "Planning"
    elif "bug" in text or "error" in text:
        return "Debugging"
    elif "email" in text or "call" in text:
        return "Communication"
    else:
        return "General"

def extract_place_and_time(text: str):
    doc = nlp(text)
    place = None
    time = None
    
    for ent in doc.ents:
        if ent.label_ == "GPE":  
            place = ent.text
    
    if place is None:
        place_match = re.search(r"\b(?:in|at|from)\s+([A-Za-z\s]+)\b", text)
        if place_match:
            place = place_match.group(1).strip()

    for ent in doc.ents:
        if ent.label_ == "TIME" or ent.label_ == "DATE":
            try:
                time = parser.parse(ent.text)
            except ValueError:
                continue
    
    if time is None:
        try:
            time = parser.parse(text, fuzzy=True)
        except ValueError:
            pass

    return place, time

def analyze_task_text(text: str):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    category = "General"
    if "doctor" in [ent.text.lower() for ent in doc.ents]:
        category = "Healthcare"

    return {
        "category": category,
        "entities": entities,
        "tokens": [token.text for token in doc]
    }
