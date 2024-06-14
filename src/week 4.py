import csv
import os

def load_data(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(row) for row in reader]

def save_data(filename, data):
    fieldnames = data[0].keys() if data else []
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Define file paths
base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
data_dir = os.path.join(base_dir, '..', 'data')
products_file = os.path.join(data_dir, 'products.csv')
couriers_file = os.path.join(data_dir, 'couriers.csv')
orders_file = os.path.join(data_dir, 'orders.csv')
orders_status_file = os.path.join(data_dir, 'order_status.csv')

def main_menu():
    print("\----Main Menu------")
    print("1. Product")
    print("2. Couriers")
    print("3. Orders")
    print("0. Exit")

# ---------products inventory Management---------

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
            # View product inventory
            print("----Products----")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
           
            exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
            if exit_choice == 'e':
                exit()

        elif choice == '2':
            # Add new product to list
            product_name = input("Enter name: ")
            product_price = float(input("Enter price: "))

            new_product = {"name": product_name, "price": product_price}
            products.append(new_product)

            print("----Products----")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
            print(f"'{product_name}' added to product list.")

        elif choice == '3':
            # Update an existing product list
            print("----Products----")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
            index = int(input("Product index to update: ")) - 1
            product = products[index]
            for key in product:
                updated_product = input(f"Enter new {key} (or leave blank to keep current '{product[key]}'): ")
                if updated_product:
                    product[key] = float(updated_product) if key == 'price' else updated_product
            print("Product has been updated.")

        elif choice == '4':
            # Delete product via index
            print("----Products----")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
            index = int(input("Product index to delete: ")) - 1
            products.pop(index)
            print("Product has been deleted.")
        else:
            print("Invalid choice. Try again.")

# --------couriers menu--------

# order_status = ["Preparing", "Out for delivery", "Delivered"]

def display_courier_inventory():
    print("\nCourier Management")
    print("1. View")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("0. Return to Main Menu")

def manage_courier_inventory(couriers):
    while True:
        display_courier_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # view list of current couriers
            print("----Couriers----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier['name']},  {courier['phone']}")

            exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
            if exit_choice == 'e':
                exit()

        elif choice == '2':
            # add a new courier to list
            courier_name = input("Enter courier name: ")
            courier_phone = input("Enter courier phone number: ")
            courier = {"name": courier_name, "phone": courier_phone}
            couriers.append(courier)
            print(f"Courier '{courier_name}' added to courier list.")

        elif choice == '3':
            # update existing courier
            print("----Couriers----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}:  {courier['name']},  {courier['phone']}")
            try:
                index = int(input("Courier index to update: ")) - 1
                if index < 0 or index >= len(couriers):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            courier = couriers[index]
            for key in courier:
                updated_courier = input(f"Enter new {key} (or leave blank to keep current '{courier[key]}'): ")
                if updated_courier:
                    courier[key] = updated_courier
            print("Courier has been updated.")

        elif choice == '4':
            # delete a courier
            print("----Couriers----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}:  {courier['name']},  {courier['phone']}")
            try:
                index = int(input("Courier index to delete: ")) - 1
                if index < 0 or index >= len(couriers):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            couriers.pop(index)
            print("Courier has been deleted.")
        else:
            print("Invalid choice. Try again.")
        break

# -----------Order Management----------- 

def order_inventory():
    print("\----Order Catalogue----")
    print("1. View")
    print("2. Add")
    print("3. Update Existing Status")
    print("4. Update Existing Order")
    print("5. Delete")
    print("0. Return to Main Menu")

def order_system(orders,products, couriers):
    while True:
        order_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # View orders list
            print("----Orders----")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")

            exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
            if exit_choice == 'e':
                exit()
            elif exit_choice == '0':
                continue

        elif choice == '2':
            # Add new customer order
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            customer_phone = input("Enter customer phone: ")
            
            print("----Products----")
            for i, product in enumerate(products):
                print(f"{i + 1}: {product['name']} at ${product['price']}")
            items = input("Enter product indexes (comma-separated): ")
            
            
            print("----Couriers----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")
            courier_index = int(input("Enter courier index: ")) - 1
            
            order_list = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "courier": courier_index,
                "status": "preparing",
                "items": items
            }
            orders.append(order_list)
            print("Order added.")

        elif choice == '3':
            # Update an existing order status
            print("----Orders---")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            try:
                index = int(input("Order index to update status: ")) - 1
                if index < 0 or index >= len(orders):
                    print("Invalid index. Please try again.")
                   
            except ValueError:
                print("Invalid. Please enter a number.")
                continue
            
            print("---Order status----")
            for i, status in enumerate(order_status):
                print(f"{i + 1}: {status}")
            try:
                status_index = int(input("Enter status index: ")) - 1
                if status_index < 0 or status_index >= len(order_status):
                    print("Invalid status index. Please try again.")
                    continue
            except ValueError:
                print("Invalid. Please enter a number.")
                continue
            
            orders[index]['status'] = order_status[status_index]
            print("Order status updated.")

        elif choice == '4':
            # Update an existing order
            print("----Orders----")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            try:
                index = int(input("Enter order index to update: ")) - 1
                if index < 0 or index >= len(orders):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid. Please enter a number.")
                continue

            order = orders[index]
            for key in order:
                updated_order = input(f"Enter new {key} (or leave blank to keep current '{order[key]}'): ")
                if updated_order:
                    order[key] = updated_order 
            print("Order updated.")

        elif choice == '5':
            # Delete an order
            print("----Orders----")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            try:
                index = int(input("Order index to delete: ")) - 1
                if index < 0 or index >= len(orders):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid. Please enter a number.")
                continue
            orders.pop(index)
            print("Order deleted.")
        else:
            print("Invalid. Try again.")
        break


#------Main Eexcution -------

if __name__ == "__main__":
    # Load data from CSV files
    products = load_data(products_file)
    couriers = load_data(couriers_file)
    orders = load_data(orders_file)
    order_status = load_data(orders_status_file)
    #order_status = load_data(order_status_file)
    
    while True:
        main_menu()
        options = input("Enter options: ")
        if options == '1':
            manage_product_catalogue(products)
        elif options == '2':
            manage_courier_inventory(couriers)
        elif options == '3':
            order_system(orders, products, couriers)
        elif options == '0':
            save_data(products_file, products)
            save_data(couriers_file,couriers)
            save_data(orders_file, orders)
            save_data(orders_status_file, order_status)
            break
        else:
            print("Invalid choice. Please try again.")