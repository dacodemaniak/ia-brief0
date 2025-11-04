import streamlit as st
import requests
from loguru import logger

what_to_analyse = "Bonjour Jean-Luc, comment vas-tu ?"




st.title("Sentiment analysis")


client_input = st.text_input(label="What would you say")


if (st.button("Call BoB")): 
    if client_input: 
        logger.info(f"Client input was : {client_input}")

        try: 
            response = requests.post("http://127.0.0.1:9000/sentiment_analysis/", json={"texte": client_input})
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

        except requests.exceptions.RequestException as e:
            st.error(f"Connexion to API failed : {e}")
            logger.error(f"Connexion to API failed : {e}")
        except Exception as e:
            st.error(f"Something went wrong : {e}")
            logger.error(f"Something went wrong : {e}")
    else: 
        st.write("Please, let me help u with a text")