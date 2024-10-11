import pandas as pd
import pathlib

def some_function(argument1):
     """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
     """
     pass


if __name__ == '__main__':
    file_path = pathlib.Path(__file__).parent.parent.joinpath("data","paralympics_events_raw.csv")
    df = pd.read_csv(file_path)
    print(df.head())
