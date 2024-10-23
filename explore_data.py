from fetch_data import fetch_weather_data

def explore_data():
    data = fetch_weather_data()

    # Display basic information about the dataset
    print(data.info())

    # Get summary statistics
    print(data.describe())

    # Check for missing values
    print(data.isnull().sum())

if __name__ == "__main__":
    explore_data()
