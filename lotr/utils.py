import json
import typing
import requests
from lotr.error import CustomError

# urls
LOTR_API_URL = "https://the-one-api.dev/v2"
RETRY_STATUS_CODES = [429, 500, 502, 503, 504]

# pkg metadata
API_VERSION = "1"
END_POINT = "/movie/"

def auth_formatter(key):
    'builds the header for authentication purposes'
    return {'Authorization': f'Bearer {key}'}

def is_api_key_valid(key: typing.Optional[str]) -> bool:
    'checks if API key is valid, if not returns a message denoting so.'
    if not key:
        raise CustomError(
            "No API key provided. Provide the API key or the LOTR_API_KEY environment variable."  # noqa: E501
        )
    try:
        resp = requests.get(
            url = f'{LOTR_API_URL}+{END_POINT}',
            headers= auth_formatter(key), timeout=5
        )
    except:
        resp = None

    return resp and resp.status_code == 200 