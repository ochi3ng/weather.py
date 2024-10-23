import requests
import mysql.connector
from mysql.connector import Error

# Function to fetch weather data from OpenWeatherMap
def fetch_weather_data_from_openweathermap(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to store weather data into MySQL
def store_weather_data(connection, data, city, source):
    cursor = connection.cursor()

    # Check if the data contains the required fields
    if 'main' not in data or 'wind' not in data or 'weather' not in data:
        print(f"Error fetching weather data for {city}: Invalid data format.")
        return

    # Extract data from OpenWeatherMap response
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    # Insert data into the WeatherData table
    cursor.execute("""
        INSERT INTO WeatherData (city, temperature, humidity, pressure, wind_speed, description, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (city, temp, humidity, pressure, wind_speed, description, source))

    # Commit the transaction
    connection.commit()

    print(f"Stored weather data for {city}: Temp={temp}°C, Humidity={humidity}%, Pressure={pressure} hPa, Wind Speed={wind_speed} m/s, Description={description}")

    cursor.close()

# Main function to fetch and store data
def main():
    # MySQL connection details
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='John480220.',
            database='weather_db'
        )

        if connection.is_connected():
            print("Successfully connected to the database.")

            # Your OpenWeatherMap API key
            api_key = "fb77bc89a334b136d42e29e305350e3e"

            # List of cities in Kenya
            cities = ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]

            # Fetch and store data for each city
            for city in cities:
                weather_data = fetch_weather_data_from_openweathermap(city, api_key)
                store_weather_data(connection, weather_data, city, "OpenWeatherMap")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
