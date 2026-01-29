import aiohttp
    
async def get_data_for_url(session: aiohttp.ClientSession, url: str) -> dict:
        async with session.get(url) as response:
            data = response.json()
        return data

