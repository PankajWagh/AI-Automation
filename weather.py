
from fastmcp import FastMCP
import requests

app = FastMCP("WeatherServer")

@app.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    response = requests.get(f"https://wttr.in/{city}?format=3")
    return response.text

if __name__ == "__main__":
   app.run(transport="sse", host="127.0.0.1", port=8000)

