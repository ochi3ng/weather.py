import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def fetch_weather_data():
    # MySQL connection setup using environment variables
    db_connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    # Query to fetch data from the WeatherData table
    query = "SELECT * FROM WeatherData"
    weather_data = pd.read_sql(query, db_connection)

    # Close the connection
    db_connection.close()

    return weather_data
