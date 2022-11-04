# Author: Nathan
# Contains functions to validate input.


from typing import List
from typing import Union


def check_index(list_to_check: List, input: str) -> bool:
    """Validates the input as an index and returns an appropriate boolean

    Args:
        list_to_check (List): The list to check the index against.
        input (str): The index to be checked.

    Returns:
        bool: True if the index is valid, False if not.
    """
    try:
        index = int(input)
        index -= 1
        list_to_check[index]
    except IndexError:
        print('This order does not exist.')
        return False
    except ValueError:
        print('Input cannot be converted into an integer.')
        return False
    return True


def get_input_index(option: str, action: str,
                    list_to_check: List) -> Union[int, None]:
    """Contains a while loop with an input function that asks for user input,
    and returns an index once you input a valid index.

    Args:
        option (str): The object type that the user wants to modify.
        action (str): What the user wants to do to the object.
        list_to_check (List): The list to check the index against.

    Returns:
        int: The index of the list object, e.g Item No.1 = Index 0
        None: If the index is zero.
    """
    while True:  # Doesn't break from loop until valid input.
        index = (input(f'Type the index of the'
                       f' {option} you wish to {action}: '))
        if index == '0':
            return None
        elif check_index(list_to_check, index):
            return int(index) - 1
        else:
            continue
