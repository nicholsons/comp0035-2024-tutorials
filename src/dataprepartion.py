from pathlib import Path
import pandas as pd


def describe_dataframe(dataframe):
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
    """
    print(dataframe.shape)
    pd.set_option("display.max_columns", None)

    print(dataframe.head(5))
    print(dataframe.tail(5))
    print(dataframe.columns)
    print(dataframe.dtypes)
    print(dataframe.info)


    description = ""
    return description

def prepare_dataframe(dataframe):
    float_columns = dataframe.select_dtypes(include=['float'])
    for column in float_columns: 
        dataframe[column] = dataframe[column].astype('int')
    return dataframe

if __name__ == '__main__':

    project_root = Path(__file__).parent
    csv_file = project_root.joinpath('tutorialpkg', 'data', 'paralympics_events_raw.csv')
    df = pd.read_csv(csv_file)
    describe_dataframe(df)

    excel_file = project_root.joinpath('tutorialpkg', 'data', 'paralympics_all_raw.xlsx')
    df2 = pd.read_excel(excel_file, sheet_name=1)
    describe_dataframe(df2)

    df3 = pd.read_excel(excel_file, sheet_name= "medal_standings")
    describe_dataframe(df3)

    #prepare_dataframe(df)

    print("Start column values:", df['start'])
    print("End column values:", df['end'])










