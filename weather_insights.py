import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="John480220.",
    database="weather_db"
)

# Fetch weather data from the database
weather_data = pd.read_sql("SELECT * FROM WeatherData", db_connection)

# Convert timestamp to datetime format
weather_data['timestamp'] = pd.to_datetime(weather_data['timestamp'])

# Step 1: Analyze Temperature Trends Across Regions
plt.figure(figsize=(10, 6))
sns.lineplot(x='timestamp', y='temperature', hue='city', data=weather_data)
plt.title("Temperature Trends by City/Region")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 2: Analyze Rainfall Patterns (if Rain Data Available)
plt.figure(figsize=(10, 6))
sns.lineplot(x='timestamp', y='rainfall', hue='city', data=weather_data)
plt.title("Rainfall Patterns by City/Region")
plt.xlabel("Timestamp")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 3: Analyze Humidity Trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='timestamp', y='humidity', hue='city', data=weather_data)
plt.title("Humidity Trends by City/Region")
plt.xlabel("Timestamp")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 4: Analyze Pressure Trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='timestamp', y='pressure', hue='city', data=weather_data)
plt.title("Pressure Trends by City/Region")
plt.xlabel("Timestamp")
plt.ylabel("Pressure (hPa)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Analyze Correlation Between Weather Variables
corr_matrix = weather_data[['temperature', 'humidity', 'pressure', 'rainfall']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation between Weather Variables")
plt.show()

# Step 6: Seasonal Analysis (Extract Month)
weather_data['month'] = weather_data['timestamp'].dt.month

avg_temp_by_month = weather_data.groupby('month')['temperature'].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x=avg_temp_by_month.index, y=avg_temp_by_month.values)
plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
