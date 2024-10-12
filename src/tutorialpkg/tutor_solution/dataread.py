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
    file_path1 = pathlib.Path(__file__).parent.parent.joinpath("data","paralympics_events_raw.csv")
    df1 = pd.read_csv(file_path1)
    # print(df1.head())

    file_path2 = pathlib.Path(__file__).parent.parent.joinpath("data","paralympics_all_raw.xlsx")
    df2 = pd.read_excel(file_path2)
    # print(df2.head())

    df3 = pd.read_excel(file_path2, sheet_name = "medal_standings")
    print(df3.head())


