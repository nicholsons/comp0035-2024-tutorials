import pathlib
import pandas as pd


def some_function(argument1):
     """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
     """
if __name__ == '__main__':
     pth = pathlib.Path(__file__)
     print(pth)
     paralympics_datafile_excel = pth.parent.joinpath("tutorialpkg").joinpath("data", "paralympics_all_raw.xlsx")
     paralympics_events_raw_csv = pth.parent.joinpath("tutorialpkg").joinpath("data", "paralympics_events_raw.csv")
     if(paralympics_datafile_excel.exists):
          print("file exists")
     else:
          print("file not exists")
     pd.read_excel(paralympics_datafile_excel)
 