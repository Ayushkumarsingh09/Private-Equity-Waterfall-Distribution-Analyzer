import matplotlib.pyplot as plt
import pandas as pd

def plot_distribution(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['PreferredReturn'], label='Preferred Return', color='blue')
    plt.plot(data['Year'], data['LP_Distribution'], label='LP Distribution', color='green')
    plt.plot(data['Year'], data['CarriedInterest'], label='Carried Interest', color='red')
    plt.title("Waterfall Distribution Over Time")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.savefig("data/outputs/charts/distributions_chart.png")
    plt.show()

if __name__ == "__main__":
    waterfall_data = pd.read_csv("data/outputs/waterfall_distribution.csv")
    plot_distribution(waterfall_data)
