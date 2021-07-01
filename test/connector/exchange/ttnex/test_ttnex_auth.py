import asyncio
import unittest
from typing import List

import conf
from hummingbot.connector.exchange.ttnex.ttnex_auth import TtnexAuth
from hummingbot.connector.exchange.ttnex.ttnex_websocket import TtnexWebsocket


class TestAuth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ev_loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        api_key = conf.ttnex_api_key
        cls.auth = TtnexAuth(api_key)
        cls.ws = TtnexWebsocket(cls.auth)

    async def con_auth(self):
        await self.ws.connect()
        await self.ws.subscribe("user-balance")

        async for response in self.ws.on_message():
            if (response.get("method") == "subscribe"):
                return response

    def test_auth(self):
        result: List[str] = self.ev_loop.run_until_complete(self.con_auth())
        assert result["status"] is True
