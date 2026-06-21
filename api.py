from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

happy_words = {
    "love", "great", "excellent", "awesome", "good", "happy",
    "wonderful", "amazing", "fantastic", "like", "best"
}

sad_words = {
    "sad", "terrible", "awful", "bad", "hate",
    "worst", "angry", "upset", "disappointed", "horrible"
}

@app.post("/sentiment")
def sentiment(req: SentimentRequest):
    results = []

    for sentence in req.sentences:
        text = sentence.lower()

        happy_score = sum(word in text for word in happy_words)
        sad_score = sum(word in text for word in sad_words)

        if happy_score > sad_score:
            label = "happy"
        elif sad_score > happy_score:
            label = "sad"
        else:
            label = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": label
        })

    return {"results": results}
