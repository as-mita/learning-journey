import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        data = response.json()

        # Extract main details
        current = data["current_condition"][0]
        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        desc = current["weatherDesc"][0]["value"]

        print(f"\n🌤 Weather in {city.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc}\n")

    except Exception as e:
        print("Error fetching weather. Check city name or Internet connection.")


def main():
    print("=== Weather CLI App ===")
    print("Type 'exit' to quit")

    while True:
        city = input("\nEnter city name: ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        if city.strip() == "":
            print("Please enter a valid city.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
