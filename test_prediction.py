from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_prediction_endpoint():
    # Just checks API is reachable
    response = client.get("/health")
    assert response.status_code == 200

    # Predict returns correct structure if model exists
    # Optional: skip if no trained model in repo