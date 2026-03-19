import asyncio
from mcp import StdioServerParameters
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client

async def main():
    server = StdioServerParameters(
        command="python",
        args=["weather.py"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool("get_weather", {"city": "Pune"})
            print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())