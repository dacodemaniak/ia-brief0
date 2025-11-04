from fastapi import FastAPI, HTTPException
from loguru import logger
from nltk.sentiment import SentimentIntensityAnalyzer
from pydantic import BaseModel
from nltk.data import load
import nltk

app = FastAPI()

logger.add("logs/sentiment_api.log", rotation="500 MB", level="INFO")
class Texte(BaseModel):
    texte: str

@app.get('/')
async def root():
    logger.info("Route '/' was called")
    return {"message": "Hello world!"}

@app.post('/sentiment_analysis')
async def sentiment_analysis(input: Texte):
    nltk.download('vader_lexicon', quiet=True)

    sia = SentimentIntensityAnalyzer()

    sentiment = sia.polarity_scores(input.texte)

    logger.info(f"Results: {sentiment}")

    return {
        "neg": sentiment["neg"],
        "neu": sentiment["neu"],
        "pos": sentiment["pos"],
        "compound": sentiment["compound"]
    }