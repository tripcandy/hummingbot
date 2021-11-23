import json
import asyncio
import aiohttp
from aiohttp import web

# Constants
PRICE_URL = "https://api.pancakeswap.info/api/v2/tokens/0x639ad7c49ec616a64e074c21a58608c0d843a8a3"
price = "0.0"


# price fetcher
async def fetch_price():
    async with aiohttp.ClientSession() as client:
        async with client.get(f"{PRICE_URL}", timeout=10) as response:
            try:
                parsed_response = json.loads(await response.text())
                result = parsed_response["data"]["price"]
            except Exception as e:
                raise e

            return result

# price api handler
async def price_api(request):
    global price

    try:
        new_price = await fetch_price()
        if new_price is not None:
            price = new_price
    except Exception as e:
        print(e)

    return web.Response(text=price)


app = web.Application()
app.router.add_get('/', price_api)

web.run_app(app, port=2357)
