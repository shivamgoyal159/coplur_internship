import requests

def weather_details(city,api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = f"{url}q={city}&appid={api_key}&units=metric"
    print(final_url)

    try:
        requests.get(final_url)
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"Weather is {city}:")
        print(f"Temperature: {temperature}C(feels like: {feels_like}C")
        print(f"Humidity: {humidity}%")
        print(f"Descrition: {data["weather"][0]["description"].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

api_key ="30f5f498611580da50a52d18563261b6"
city = input("enter city name:")

weather_details(city,api_key)

