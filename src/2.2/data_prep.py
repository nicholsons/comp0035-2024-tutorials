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
     #task2.04 dtype
     events_csv_df['start'] = pd.to_datetime(events_csv_df['start'], format='%d/%m/%Y')
     events_csv_df['end'] = pd.to_datetime(events_csv_df['end'], format='%d/%m/%Y')
     columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
     events_csv_df[columns_to_change] = events_csv_df[columns_to_change].fillna(0).astype(int)
     
     #task2.05 merge
     npc_codes_df = pd.read_csv(path_to_npc_csv_file, usecols=['Name', 'Code'], encoding='utf-8', encoding_errors='ignore')
     merged_df = events_csv_df.merge(npc_codes_df, how='left', left_on='country', right_on='Name')
     print(merged_df[['country', 'Code', 'Name']])

     return events_csv_df
     #task2.06 removing cols
     events_csv_df = events_csv_df.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)

     #task2.07 dealing missing values
     #delate useless column
     # events_csv_df = events_csv_df.drop(columns=['Name'], axis=1)
     # 填充 participants_m 和 participants_f 的缺失值
     events_csv_df['participants_m'].fillna(method='ffill', inplace=True)
     events_csv_df['participants_f'].fillna(method='ffill', inplace=True)
     # 删除未来年份的行并重置索引
     events_csv_df = events_csv_df.drop(index=[0, 17, 31])
     events_csv_df.reset_index(drop=True, inplace=True)

     # 替换国家名称
     replacement_names = {
          'UK': 'Great Britain',
          'USA': 'United States of America',
          'Korea': 'Republic of Korea',
          'Russia': 'Russian Federation',
          'China': "People's Republic of China"
     }
     events_csv_df['country'] = events_csv_df['country'].replace(replacement_names)


     #task2.08
     # 移除 'type' 列中每个值的前后空格
     events_csv_df['type'] = events_csv_df['type'].str.strip()

     # 将 'type' 列中的值转换为小写
     events_csv_df['type'] = events_csv_df['type'].str.lower()
     
     #task2.09 Adding new columns
     events_csv_df['start'] = pd.to_datetime(events_csv_df['start'])
     events_csv_df['end'] = pd.to_datetime(events_csv_df['end'])

     # 计算持续时间并将新列插入到 'end' 列之后
     events_csv_df.insert(events_csv_df.columns.get_loc('end') + 1, 'duration', (events_csv_df['end'] - events_csv_df['start']).dt.days.astype(int))
     
     return events_csv_df


if __name__ == '__main__':
     pth = pathlib.Path(__file__)
     try:
          paralympics_datafile_csv = pth.parent.parent / 'tutorialpkg' / 'data' / 'paralympics_events_raw.csv'
          path_to_npc_csv_file = pth.parent.parent /'tutorialpkg/data/npc_codes.csv'
          events_csv_df = pd.read_csv(paralympics_datafile_csv)
          # df_romved_cols = removing_cols(events_csv_df)
          # print(df_romved_cols)
          # events_csv_df = dealing_missing_values(events_csv_df)
          # print(events_csv_df.isna().sum())
          events_csv_df = prepare_data(events_csv_df)
          print(events_csv_df)
     except FileNotFoundError as e:
          print(f"File not found. Please check the file path. Error: {e}")

     # Read the data from the file into a Pandas dataframe
     
     # prepare_data(events_csv_df)
     # describe_dataframe(events_csv_df)
     # merged_df(events_csv_df)
     
     
     
     

     
     



