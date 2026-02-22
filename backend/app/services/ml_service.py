import requests
from typing import List

ML_SERVICE_URL = "http://127.0.0.1:8001/predict"


def call_ml_service(symptoms: List[str]) -> dict:
    """
    Calls the external ML microservice and returns prediction result.
    """

    try:
        response = requests.post(
            ML_SERVICE_URL,
            json={"symptoms": symptoms},
            timeout=10  # prevents hanging requests
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        raise Exception("ML Service Timeout")

    except requests.exceptions.ConnectionError:
        raise Exception("Cannot connect to ML Service. Is it running on port 8001?")

    except requests.exceptions.HTTPError as e:
        raise Exception(f"ML Service HTTP Error: {str(e)}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"ML Service Error: {str(e)}")
