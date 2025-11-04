# Sentiment analysis

## Requirements

- nltk
- fastapi
- uvicorn
- streamlit
- requests
- pydantic
- loguru

## Git repository

[Dacodemaniak - Jean-Luc](https://github.com/dacodemaniak/ia-brief0.git)

## After cloning

`pip install -r requirements.txt`

## Run the API

`uvicorn sentiment_api:app --host 127.0.0.1 --port 9000 --reload``

## Run Client

`streamlit run sentiment_streamlit.py``


## Changelog

- [1.0.0]
    - root endpoint to test API availability : GET /
    - sentiment_analysis to run analysis : POST /sentiment_analysis
    - streamlit simple IHM
