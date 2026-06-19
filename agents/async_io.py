pip install aiohttp
import asyncio
import aiohttp

async def fetch_weather_async(city):
  print(f"Fetching weather for {city}")
  # Simulate an I/O-bound operation, like a network request
  await asyncio.sleep(2) # 2 sec each, but run concurrently
  return f"Async weather data for {city}"

async def main_async():
  cities = ['New York', 'London', 'Paris']

  start = time.time()

  # Create a list of tasks for each city
  tasks = [fetch_weather_async(city) for city in cities]

  # Run all tasks concurrently
  weather_data = await asyncio.gather(*tasks)

  for data in weather_data:
    print(data)

  print(f"Time taken (async):", round(time.time() - start, 2), "seconds")

# Run the asynchronous main function
await main_async()
