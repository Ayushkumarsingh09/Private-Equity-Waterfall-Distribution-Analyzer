import pytest
import pandas as pd
from src.visualization import plot_distribution

def test_plot_distribution():
    data = pd.DataFrame({
        "Year": [1, 2],
        "PreferredReturn": [80000, 160000],
        "LP_Distribution": [70000, 140000],
        "CarriedInterest": [50000, 100000]
    })

    # Test if the function executes without error
    try:
        plot_distribution(data)
        assert True
    except Exception as e:
        pytest.fail(f"Plotting failed with error: {e}")
