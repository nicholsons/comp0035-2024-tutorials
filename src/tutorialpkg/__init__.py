import pandas as pd
import pathlib

def some_function(argument1):
     """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
     """


if __name__ == '__main__':
    file_path = pathlib.Path(__file__)
    file1 = pd.read_csv('data\paralympics_events_raw.csv')

