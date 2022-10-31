
# Input what you are saving and what it is, no return value
def save_data(option):
    match option:
        case 'product':
            try:
                with open('GenerationProject\data.txt', 'w') as file:
                    file.write('Apple\n')
                    file.write('Banana\n')
            except:
                pass
        case 'courier':
            pass
        case 'order':
            pass
        case _:
            pass
    pass

# Input what you want to load, return what is loaded.
def load_data(option):
    match option:
        case 'product':
            pass
        case 'courier':
            pass
        case 'order':
            pass
        case _:
            pass
    pass