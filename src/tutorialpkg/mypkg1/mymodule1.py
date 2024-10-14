from math import sqrt  # import the sqrt module from the math package
import math  # import the math package
from pathlib import Path

from flake8 import exceptions  # third party dependency

from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle  # local application import

from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data
mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using pathlib.Path. Prove it exists.


    # This script is located in a subfolder so you need to navigate up to the parent (src) and then its parent (project root), then down to the 'data' directory and finally the .csv file
    csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_prepared.csv')
    print(Path(__file__))
    # Check if the file exists
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")
