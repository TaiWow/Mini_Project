
# Products Catalogue Management
products = ["Cherry Berry", "Savory Surprise", "Strawberry Peach", "Coconut Lime", "Vanilla Chai"]

def product_management_system():
    print("----Product Management System---- ")
    print("1. Product List")
    print("2. Add New Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("0. Return to Main Menu")

def manage_product_catalogue(products):
    while True:
        product_management_system()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # view product catalogue
            print("----Products List----")
            for i, product in enumerate(products):
                print(f"{i + 1}  : {product}")

            exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
            if exit_choice == 'e':
                exit()

        elif choice == '2':
            # Adds new product to list
            new_product = input("Enter new product to list: ")
            products.append(new_product)
            print(f" '{new_product}' added to product list .")

        elif choice == '3':
            # updates an existing product list
            print("----Products List----")
            for i, product in enumerate(products):
                print(f"{i + 1}  : {product}")

            index = int(input("product index to update: ")) - 1
            update_product = input("Enter updated product name: ")

            products[index] = update_product
            
            print(f"Product has been updated to '{update_product}'.")

        elif choice == '4':
            # deletes product via index
            print("----Products List----")
            for i, product in enumerate(products):
                print(f"{i + 1}: {product}")

            index = int(input("Product index to delete: ")) - 1
            products.pop(index)
            print("Product has been deleted.")
        else:
            print("Invalid. Try again.")
            


if __name__ == "__main__":
     manage_product_catalogue(products)




