import requests
import mysql.connector
from mysql.connector import Error

# Function to fetch weather data from WeatherAPI
def fetch_weather_data_from_weatherapi(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()

# Function to store weather data into MySQL
def store_weather_data(connection, data, city, source):
    cursor = connection.cursor()

    # Check if data fetching was successful
    if 'current' not in data:
        print(f"Error fetching weather data for {city}: {data.get('error', {}).get('message', 'No message available')}")
        return

    # Extract data from WeatherAPI
    temp = data['current']['temp_c']
    humidity = data['current']['humidity']
    precipitation = data['current'].get('precip_mm', 0)  # Precipitation in mm

    # Insert data into the WeatherData table
    cursor.execute("""
        INSERT INTO WeatherData (city, temperature, humidity, precipitation, source)
        VALUES (%s, %s, %s, %s, %s)
    """, (city, temp, humidity, precipitation, source))

    # Commit the transaction
    connection.commit()

    print(f"Stored weather data for {city}: Temp={temp}°C, Humidity={humidity}%, Precipitation={precipitation} mm, Source={source}")

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

            # Your WeatherAPI key
            api_key = "bc421c23b46f4395878154307240910"

            # List of cities in Kenya
            cities = ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]

            # Fetch and store data for each city
            for city in cities:
                weather_data = fetch_weather_data_from_weatherapi(city, api_key)
                store_weather_data(connection, weather_data, city, "WeatherAPI")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
