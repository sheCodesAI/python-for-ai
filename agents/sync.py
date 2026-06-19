import time 
#Subroutines

def fetch_weather_sync(city):
  print(f"Fetching weather for {city}")
  time.sleep(2) # 2 sec each for each 3 cities
  return f"weather data for {city}"

cities = ['New York', 'London', 'Paris']

start = time.time()

for city in cities:
  weather = fetch_weather_sync(city)
  print(weather)

print(f"Time taken:" , round(time.time() - start, 2), "seconds")
