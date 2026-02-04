from transformers import pipeline

# Load sentiment / intent model from Hugging Face
nlp_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_text(text: str):
    """
    Analyze user text and return intent-like output
    """
    result = nlp_pipeline(text)[0]

    intent = "set_reminder" if result["label"] == "POSITIVE" else "unknown"

    return {
        "intent": intent,
        "confidence": result["score"],
        "text": text
    }
