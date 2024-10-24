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
    """Summary or Description of the Function
 
        Parameters:
        argument1 (int): Description of arg1
 
        Returns:
        int:Returning value
 
    """
    #print("Start column values:", df['start'])
    #print("End column values:", df['end'])

    #change the date formats using the pandas function

    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])

    #print("Start column values:", df['start'])
    #print("End column values:", df['end'])

    #drop columns
    df_prepared = dataframe.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)
    print(df_prepared.columns)

     #create a dataframe with missing rows of df_prepared
    #missing_rows = df[df_prepared.isna().any(axis=1)]
    #missing_columns = df[df_prepared.isna().any(axis=0)]

    #drop row 0
    df_prepared = df_prepared.drop(index=[0, 17, 31])

    #covert float columns to int
    float_columns = df_prepared.select_dtypes(include=['float'])
    for column in float_columns: 
        df_prepared[column] = df_prepared[column].astype('int')

    #strip whitespace from the 'type' column
    df['type'] = df['type'].str.strip()
    #change all the values in the 'type' column to lowercase
    df['type'] = df['type'].str.lower()

    #add a new column called duration which can be calculated by subtracting the start date from the end, after the end column 
    #df_prepared['duration'] = df_prepared['end'] - df_prepared['start']
    #insert the duration column after the end column
    df_prepared.insert(df_prepared.columns.get_loc('end'), 'duration', df_prepared['end'] - df_prepared['start'])
    #convert the duration column to days
    df_prepared['duration'] = df_prepared['duration'].dt.days.astype(int)

    
    #save the output to file in the 'data' directory in tutorialpkg
    df_prepared.to_csv(project_root.joinpath('tutorialpkg', 'data', 'paralympics_events_prepared.csv'), index=False)

    return df_prepared

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

    prepare_dataframe(df)
    
    #print unique values for the 'type' column
    print(df['type'].unique())
    print(prepare_dataframe(df))
    


    
    


