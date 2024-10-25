from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd


if __name__ == '__main__':
    # Create a connection to the database
    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'temporary.db')
    engine = create_engine('sqlite:///' + str(db_path), echo=True)

    # Read the data from the CSV file into a DataFrame
    data_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')
    df = pd.read_csv(data_path)

    # Write the data to the database using sqlalchemy as the engine and connection
    with engine.begin() as connection:
        df.to_sql('my_table_name', connection, if_exists='replace', index=False)