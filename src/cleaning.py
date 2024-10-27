import numpy as np
import pandas as pd

def clean_data(input: list, id: str)->pd.DataFrame: 
    """
    This function cleans the input data. 
    Entries that dont have a valid ID column entry will be removed. 

    args: 
        input (list): list of the raw data
        id (str): ID column

    returns: 
        pd.DataFrame 
    """

    # Clean the DataFrame: Replace None and empty strings with 'NA'
    input.replace('', np.nan, inplace=True)  # Replace empty strings with 'NA'
    input.fillna(np.nan, inplace=True)  # Replace None values with 'NA'

    # Drop rows that are full NA
    data = input.dropna(subset="Name")  # Drop rows where all elements are NA


    return data
