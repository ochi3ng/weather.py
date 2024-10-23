import seaborn as sns
import matplotlib.pyplot as plt
from fetch_data import fetch_weather_data

def analyze_correlation():
    data = fetch_weather_data()

    # Calculate correlation matrix
    corr_matrix = data[['temperature', 'humidity', 'pressure']].corr()
    print("Correlation Matrix:\n", corr_matrix)

    # Plot the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation between Weather Variables")
    plt.show()

if __name__ == "__main__":
    analyze_correlation()
