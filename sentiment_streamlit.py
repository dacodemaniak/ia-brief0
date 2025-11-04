import streamlit as st
import requests
from loguru import logger

what_to_analyse = "Bonjour Jean-Luc, comment vas-tu ?"
response = requests.post("http://127.0.0.1:9000/sentiment_analysis/", json={"texte": what_to_analyse})

response.raise_for_status()

sentiment = response.json()

st.write("Result analysis :")
st.write(f"Negative probability : {sentiment['neg']}")
st.write(f"Neutral probability : {sentiment['neu']}")
st.write(f"Positive polarity : {sentiment['pos']}")
st.write(f"Compound score : {sentiment['compound']}")

'''
    Synthetization
'''
if sentiment['compound'] > 0.05 :
    st.write("Global sentiment : positive 😁")
elif sentiment["compound"] <= 0.05 :
    st.write("Global sentiment : negative 🙁")
else :
    st.write("Global sentiment : neutral 😑")
    logger.info(f"Printed results : {sentiment}")