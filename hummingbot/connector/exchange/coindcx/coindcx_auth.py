import hmac
import json
import hashlib
from typing import Dict, Any


class CoindcxAuth():
    """
    Auth class required by CoinDCX API
    Learn more at https://docs.coindcx.com/#authentication
    """
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def generate_auth_headers(
        self,
        timestamp: int,
        body: Dict[str, Any] = None
    ):
        """
        Generates authentication signature and return it in a authentication header dictionary
        :return: a dictionary of auth headers the request signature
        """

        body = body or {}
        body.update({'timestamp': timestamp})

        json_body = json.dumps(body, separators = (',', ':'))

        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            json_body.encode(),
            hashlib.sha256
        ).hexdigest()

        return {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': self.api_key,
            'X-AUTH-SIGNATURE': signature
        }

    def get_headers(self) -> Dict[str, Any]:
        """
        Generates authentication headers required by crypto.com
        :return: a dictionary of auth headers
        """

        return {
            "Content-Type": 'application/json',
        }
