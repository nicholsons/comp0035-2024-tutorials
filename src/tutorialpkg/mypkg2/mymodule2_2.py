def fetch_user_data(user_id, database):
    """
    Retrieve user data from a database given a user ID.

    Parameters:
    user_id (int): The unique identifier for the user.

    Returns:
    dict: A dictionary containing user data, including keys such as 'name', 'email', and 'age'.

    Raises:
    ValueError: If the user ID is not a positive integer.

    """
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("User ID must be a positive integer.")

    return database.get(user_id, {'name': 'Unknown', 'email': 'unknown@example.com', 'age': None})
