import requests

API_KEY = "7ff26435d9f851bec133fee5bc34cd0a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}q={city}&appid={API_KEY}"

try:
    response = requests.get(request_url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    data = response.json()
    weather = data["weather"][0]['description']
    temp = round(data["main"]["temp"]-273.15, 2)
    print('Weather: ', weather)
    print('Temperature: ', temp, 'celsius')

except requests.exceptions.RequestException as e:
    print("Error: Failed to make the request:", e)
except json.JSONDecodeError as e:
    print("Error: Failed to parse JSON response:", e)
