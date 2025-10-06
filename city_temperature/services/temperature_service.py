import httpx
from typing import Optional


async def fetch_temperature(city_name: str) -> Optional[float]:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?current_weather=true&latitude=50.45&longitude=30.52"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    try:
        return data["current_weather"]["temperature"]
    except KeyError:
        return None
