# Author: Nathan
# Contains functions to validate input.


from typing import List

# Validates index, returns an appropriate boolean.
def check_index(list_to_check: List, input: str) -> bool:
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


# Gets user input, returns user input as int if it is valid
def get_input_index(option: str, action: str) -> str:
    while True:  # Doesn't break from loop until valid input.
        index = (input(f'Type the index of the'
                f' {option} you wish to {action}: '))
        if check_index(option, index):
            return int(index) - 1
        else:
            continue
