import pytest
from fastapi.testclient import TestClient
from sentiment_api import app

# Client test
client = TestClient(app)

def test_sentiment_analysis_positive(): 
    '''
        Expect a positive result
    '''
    client_request = {"texte": "I feel good today"}

    response = client.post('/sentiment_analysis', json=client_request)
    result = response.json()

    # Expect a 200 http status
    assert response.status_code == 200

    # Expect to retrieve all attributes
    assert "neg" in result
    assert "pos" in result
    assert "neu" in result
    assert "compound" in result

    # Expect all results between 0 and 1
    assert 0 <= result["neg"] <= 1
    assert 0 <= result["pos"] <= 1
    assert 0 <= result["neu"] <= 1

def test_sentiment_analysis_negative():
    '''
        Expect a positive result
    '''
    client_request = {"texte": "What a bad weather today"}

    response = client.post('/sentiment_analysis', json=client_request)
    result = response.json()

    # Expect a 200 http status
    assert response.status_code == 200

    expected_fields = ["neg", "pos", "neu", "compound"]
    for field in expected_fields:
        assert field in result
        assert isinstance(result[field], (int, float))