import pandas as pd

def calculate_waterfall(data, preferred_return=0.08, catch_up=0.2, carried_interest=0.2):
    """
    Calculate the waterfall distribution for a private equity fund.
    
    Args:
        data (pd.DataFrame): Fund cash flow data.
        preferred_return (float): Annual preferred return rate.
        catch_up (float): GP's catch-up rate.
        carried_interest (float): GP's carried interest rate.
    
    Returns:
        pd.DataFrame: Waterfall distribution breakdown.
    """
    data['PreferredReturn'] = data['CapitalContributed'].cumsum() * preferred_return
    data['DistributableCash'] = data['CapitalReturned'] + data['ProfitGenerated']
    
    data['CatchUp'] = data['DistributableCash'] * catch_up
    data['CarriedInterest'] = data['DistributableCash'] * carried_interest
    
    data['LP_Distribution'] = data['DistributableCash'] - data['CatchUp'] - data['CarriedInterest']
    return data

if __name__ == "__main__":
    # Example usage
    fund_data = pd.read_csv("data/inputs/example_fund_data.csv")
    waterfall_distribution = calculate_waterfall(fund_data)
    waterfall_distribution.to_csv("data/outputs/waterfall_distribution.csv", index=False)
