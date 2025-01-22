import pytest
import pandas as pd
from src.waterfall_calculator import calculate_waterfall

def test_calculate_waterfall():
    data = pd.DataFrame({
        "Year": [1, 2],
        "CapitalContributed": [1000000, 0],
        "CapitalReturned": [500000, 600000],
        "ProfitGenerated": [100000, 200000]
    })

    result = calculate_waterfall(data)
    assert 'PreferredReturn' in result.columns
    assert 'CatchUp' in result.columns
    assert 'CarriedInterest' in result.columns
    assert 'LP_Distribution' in result.columns
