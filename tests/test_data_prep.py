from pathlib import Path
import pandas as pd
import pytest
from tutorialpkg.tutor_solution import tutorial2_refactored


def test_save_dataframe_file_present():
    """
    GIVEN a pandas dataframe
    WHEN tutorial2_refactored.save_dataframe_to_file() is called with the correct file path and file type
    THEN the file specified should be found as a valid file in the file system
    AND reading the file into dataframe should give a dataframe contents equal to the original dataframe
    """
    df = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })
    # Arrange
    file_path_save = Path(__file__).parent.joinpath('output_df.csv')
    # Act
    tutorial2_refactored.save_dataframe_to_file(df, str(file_path_save), file_type='csv')
    # Assert
    assert file_path_save.is_file()
    read_df = pd.read_csv(file_path_save)
    assert read_df.equals(df)


# Syntax for assertions that raise an excpected exception
# https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions
def test_save_dataframe_incorrect_type_raises_error(db):
    """
    GIVEN a dataframe
    WHEN save_dataframe_to_file is called with .txt which is not supported
    THEN a ValueError should be raised with the message
    'Invalid file type. Please specify 'csv' or 'xlsx'.'
    """
    df = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })
    path_to_save = Path(__file__).joinpath('incorrect_file.txt')
    with pytest.raises(ValueError):
        tutorial2_refactored.save_dataframe_to_file(df, str(path_to_save), file_type='txt')
