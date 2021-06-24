from typing import Dict, Any


class TtnexAuth():
    """
    Auth class required by ttnex.io API
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_auth_dict(
        self,
        data: Dict[str, Any] = None
    ):
        """
        Adds API Key and return it in a dictionary along with other inputs
        :return: a dictionary of request info including the request signature
        """

        data = data or {}

        data_params = data.get('params', {})
        if not data_params:
            data['params'] = {}

        data['params'].update({'api_key': self.api_key})

        return data

    def get_headers(self) -> Dict[str, Any]:
        """
        Generates authentication headers required by ttnex.io
        :return: a dictionary of auth headers
        """

        return {
            "Content-Type": 'application/json',
        }
