import pandas as pd

def allocate_distributions(data, allocation_file):
    """
    Allocate distributions to investors based on their contribution percentage.

    Args:
        data (pd.DataFrame): Waterfall distribution data.
        allocation_file (str): Path to the CSV file with investor allocation percentages.

    Returns:
        pd.DataFrame: DataFrame with distributions allocated to each investor.
    """
    allocations = pd.read_csv(allocation_file)
    investor_distributions = {}

    for _, row in allocations.iterrows():
        investor = row['Investor']
        percentage = row['ContributionPercentage'] / 100
        investor_distributions[investor] = data['LP_Distribution'] * percentage

    allocated_data = pd.DataFrame(investor_distributions)
    allocated_data['Year'] = data['Year']
    return allocated_data

if __name__ == "__main__":
    waterfall_data = pd.read_csv("data/outputs/waterfall_distribution.csv")
    allocated_distributions = allocate_distributions(waterfall_data, "data/inputs/investor_allocation.csv")
    allocated_distributions.to_csv("data/outputs/allocated_distributions.csv", index=False)
