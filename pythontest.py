import aiohttp
import asyncio

async def main():
    # Initialize the ClientSession
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            html = await response.text()
            print("Body:", html[:15])

# Run the async session
asyncio.run(main())