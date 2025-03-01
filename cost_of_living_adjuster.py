import pandas as pd
import numpy as np

cost_of_living = pd.read_csv('https://raw.githubusercontent.com/mtran1227/NoSpendy/refs/heads/main/cost_of_living.csv')
cost_of_living = cost_of_living.sort_values(by='State').reset_index(drop=True)

def adjust_expense(expense, state, national_index=100):
    """
    Adjusts an expense based on the cost of living index for a given state.

    :param expense: The original expense to adjust (float or int).
    :param state: The name of the state (str).
    :param national_index: The national average cost of living index (default is 100).
    :return: The adjusted expense (float).
    """
    # Find the state's cost of living index
    state_data = cost_of_living[cost_of_living['State'] == state]
    
    if state_data.empty:
        raise ValueError(f"State '{state}' not found in the dataset.")
    
    state_index = state_data['Index'].values[0]
    
    # Calculate the adjusted expense
    return (expense * national_index) / state_index
