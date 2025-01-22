import pytest
import pandas as pd
from src.investor_allocation import allocate_distributions

def test_allocate_distributions():
    data = pd.DataFrame({
        "Year": [1, 2],
        "LP_Distribution": [100000, 200000]
    })

    allocation_data = pd.DataFrame({
        "Investor": ["LP1", "LP2", "GP"],
        "ContributionPercentage": [70, 20, 10]
    })

    allocation_data.to_csv("test_investor_allocation.csv", index=False)

    result = allocate_distributions(data, "test_investor_allocation.csv")
    assert "LP1" in result.columns
    assert "LP2" in result.columns
    assert "GP" in result.columns
