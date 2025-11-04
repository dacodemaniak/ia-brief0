from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores("Bonjour, je me sens plutôt bien aujourd'hui")
print(sentiment)