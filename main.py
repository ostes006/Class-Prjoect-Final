import requests

def get_weather(location):
    """Fetches weather data from openweathermap.org for the given location."""
    try:
        api_key = "10c9972af66f514eff10e0918a6c345e"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print("Invalid location. Please try again.")
            return None

        # Parse the JSON data
        data = response.json()

        # Extract the relevant information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        city = data["name"]
        
        return (city, temperature, humidity, description)
    
    except requests.exceptions.RequestException:
        print("Error: Unable to establish connection to the webservice.")
        return None

def main():
    # Ask the user for their zip code or city
    location = input("Please enter your zip code or city: ")
    
    # Fetch weather data for the location
    weather_data = get_weather(location)
    if weather_data is None:
        return
    
    # Display the weather forecast in a readable format to the user
    city, temperature, humidity, description = weather_data
    print(f"Weather forecast for {city}:")
    print(f"Temperature: {temperature:.1f} degrees Fahrenheit")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

if __name__ == "__main__":
    while True:
        main()
        # Allow the user to run the program multiple times
        run_again = input("Do you want to run the program again? (y/n) ")
        if run_again.lower() != "y":
            break