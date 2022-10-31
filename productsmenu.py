import time

# Initialise the product list, has values already in.
products = ["Pepsi", "Coca Cola", "Dr Pepper"]

# Prints out product list.
def list_products():
    i = 1
    for product in products:
        print(f"Product No.{i} {product}")
        i += 1

# This is the products menu
def products_menu():
    while True:
        print("""-----PRODUCTS-----
    0. Exit 
    1. Create Product
    2. View Product List
    3. Update Product
    4. Delete Product
---------------------""")
        option = input("Choose command: ")

        match option:
            # Exit
            case "0":
                print ("Exiting products menu...")
                time.sleep(1)
                break
            # Create Product
            case "1":
                products.append(input("Type in your product name: "))
            # View Product List
            case "2":
                print("Printing product list...")
                time.sleep(1)
                list_products()
                time.sleep(1)
            # Update Product
            case "3":
                list_products()
                index = 0
                while True:
                    try:
                        index = int(input("Type the index of the product you wish to update: ")) - 1
                        products[index]
                        break
                    except IndexError:
                        print("This product does not exist.")
                        continue
                    except ValueError:
                        print("Input cannot be converted into an integer.")
                        continue
                if (index + 1) == 0:
                    print("Selected 0, moving back to products menu.")
                    break
                updname = input(f"Type what you wish to replace {products[index]} with: ")
                print("Updating product...")
                time.sleep(1)
                products[index] = updname
                print("Updated product.")
            # Delete Product
            case "4":
                list_products()
                index = 0
                while True:
                    try:
                        index = int(input("Type the index of the product you wish to delete: ")) - 1
                        products[index]
                        break
                    except IndexError:
                        print("This product does not exist.")
                        continue
                    except ValueError:
                        print("Input cannot be converted into an integer.")
                        continue
                if (index + 1) == 0:
                    print("Selected 0, moving back to products menu.")
                    break
                print("Deleting product...")
                time.sleep(1)
                print(f"You have removed: {products.pop(index)}.")
            # Default Option, Exit Program.
            case _:
                print("No option selected, exiting program.")
                exit()
