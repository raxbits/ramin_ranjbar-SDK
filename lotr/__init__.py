from lotr.client import Client
from lotr.error import CustomError

LOTR_API_URL = "https://the-one-api.dev/v2"
RETRY_STATUS_CODES = [429, 500, 502, 503, 504]

# pkg metadata
API_VERSION = "1"
END_POINT = "/movie/"
