import pathlib
import pandas as pd

dtype_dict = {
    'column1': 'int64',
    'column2': 'float64',
    'column3': 'int64',
    # Add more columns as needed
}

def describe_dataframe(events_csv_df):
     # print(events_csv_df.shape)
     # print(events_csv_df.head , events_csv_df.tail)
     # print(events_csv_df.columns)
     print(events_csv_df.dtypes)
     # print(events_csv_df.info)
     # print(events_csv_df.describe)

def prepare_data(events_csv_df):
     events_csv_df['start'] = pd.to_datetime(events_csv_df['start'], format='%d/%m/%Y')
     events_csv_df['end'] = pd.to_datetime(events_csv_df['end'], format='%d/%m/%Y')
     columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
     events_csv_df[columns_to_change] = events_csv_df[columns_to_change].fillna(0).astype(int)
    
     return events_csv_df


if __name__ == '__main__':
     pth = pathlib.Path(__file__)
     try:
          paralympics_datafile_csv = pth.parent.parent / 'tutorialpkg' / 'data' / 'paralympics_events_raw.csv'
          path_to_npc_csv_file = pth.parent.parent /'tutorialpkg/data/npc_codes.csv'
          # cols=['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports','participants_m', 'participants_f', 'participants']
          npc_codes_df = pd.read_csv(path_to_npc_csv_file, usecols=['Name', 'Code'], encoding='utf-8', encoding_errors='ignore')
     except FileNotFoundError as e:
          print(f"File not found. Please check the file path. Error: {e}")

     # Read the data from the file into a Pandas dataframe
     events_csv_df = pd.read_csv(paralympics_datafile_csv)
     prepare_data(events_csv_df)
     describe_dataframe(events_csv_df)
     # merged_df = events_csv_df.merge(npc_codes_df, how='left', left_on='country', right_on='Name')
     # print(merged_df[['country', 'Code', 'Name']])

     
     



