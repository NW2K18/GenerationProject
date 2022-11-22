'''Author: Nathan \n
This saves the log of database transactions to a local text file.
'''

from datetime import datetime


def get_date_time() -> str:
    """Returns current time.

    Returns:
        str: Current time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def log_create(name: str):
    """Adds to the log file about creating an object.

    Args:
        name (str): Name of what is being created.
    """
    current_time = get_date_time()
    with open('data/log.txt', 'a') as file:
        file.write(f'[{current_time}]: Created {name}.\n')


def log_update(name: str):
    """Adds to the log file about creating an object.

    Args:
        name (str): Name of what is being updated.
    """
    current_time = get_date_time()
    with open('data/log.txt', 'a') as file:
        file.write(f'[{current_time}]: Updated {name}.\n')


def log_remove(name: str):
    """Adds to the log file about removing an object.

    Args:
        name (str): Name of what is being removed.
    """
    current_time = get_date_time()
    with open('data/log.txt', 'a') as file:
        file.write(f'[{current_time}]: Removed {name}.\n')
