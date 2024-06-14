# ----Imports and file handling 

import csv
import os



# Function to load data from CSV file
def load_data(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(row) for row in reader]

# Function to save data to CSV file
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

# Product Management System
def product_management_system(products):
    while True:
        print("----Product Management System---- ")
        print("1. Product List")
        print("2. Add New Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_list(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            update_product_list(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def product_list(products):
    if products:
        print("----Products----")
        for i, product in enumerate(products):
            print(f"{i + 1}: {product['name']}, ${product['price']}")
    else:
        print("No Products found.")

def add_product(products):
    try:
        product_name = input("Enter name: ")
        product_price = float(input("Enter price: "))
        new_product = {"name": product_name, "price": product_price}
        products.append(new_product)
        print(f"'{product_name}' added to product list.")
        save_data(products_file, products)  
    except ValueError:
        print("Invalid price format. Please enter a number.")

def update_product_list(products):
    try:
        product_list(products)
        index = int(input("Product index to update: ")) - 1
        product = products[index]
        for key in product:
            updated_value = input(f"Enter new {key} (or leave blank to keep current '{product[key]}'): ")
            if updated_value:
                product[key] = float(updated_value) if key == 'price' else updated_value
        print("Product has been updated.")
        save_data(products_file, products)  
    except ValueError:
        print("Invalid input format. Please enter a number.")
    except IndexError:
        print("Product index out of range. Please try again.")

def delete_product(products):
    try:
        product_list(products)
        index = int(input("Product index to delete: ")) - 1
        products.pop(index)
        print("Product has been deleted.")
        save_data(products_file, products)  # Save updated products list
    except ValueError:
        print("Invalid input format. Please enter a number.")
    except IndexError:
        print("Product index out of range. Please try again.")

# Courier Management System
def courier_management_system(couriers):
    while True:
        print("----Courier Management System---- ")
        print("1. Courier List")
        print("2. Add New Courier")
        print("3. Update Courier")
        print("4. Delete Courier")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            courier_list(couriers)
        elif choice == '2':
            add_courier(couriers)
        elif choice == '3':
            update_courier_list(couriers)
        elif choice == '4':
            delete_courier(couriers)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def courier_list(couriers):
    if couriers:
        print("----Couriers----")
        for i, courier in enumerate(couriers):
            print(f"{i + 1}: {courier['name']}, {courier['phone']}")
    else:
        print("No Couriers found.")

def add_courier(couriers):
    courier_name = input("Enter courier name: ")
    courier_phone = input("Enter courier phone number: ")
    new_courier = {"name": courier_name, "phone": courier_phone}
    couriers.append(new_courier)
    print(f"Courier '{courier_name}' and '{courier_phone}' added to courier list.")
    save_data(couriers_file, couriers)  # Save updated couriers list

def update_courier_list(couriers):
    try:
        courier_list(couriers)
        index = int(input("Courier index to update: ")) - 1
        courier = couriers[index]
        for key in courier:
            updated_value = input(f"Enter new {key} (or leave blank to keep current '{courier[key]}'): ")
            if updated_value:
                 courier[key] = updated_value
            print("Courier has been updated.")
            save_data(couriers_file, couriers)  
    except ValueError:
        print("Invalid input format. Please enter a number.")
    except IndexError:
        print("Courier index out of range. Please try again.")

def delete_courier(couriers):
    try:
        courier_list(couriers)
        index = int(input("Courier index to delete: ")) - 1
        couriers.pop(index)
        print("Courier has been deleted.")
        save_data(couriers_file, couriers)  
    except ValueError:
        print("Invalid input format. Please enter a number.")
    except IndexError:
        print("Courier index out of range. Please try again.")

# Order Management System
def order_management_system(orders, products, couriers, order_status):
    while True:
        print("----Order Catalogue----")
        print("1. Order List")
        print("2. Add an Order")
        print("3. Update Existing Order Status")
        print("4. Update Existing Order")
        print("5. Delete")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            order_list(orders)
        elif choice == '2':
            add_order(orders, products, couriers)
        elif choice == '3':
            update_order_status(orders, order_status)
        elif choice == '4':
            update_existing_order(orders)
        elif choice == '5':
            delete_order(orders)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def order_list(orders):
    print("----Orders----")
    if orders:
        for i, order in enumerate(orders):
            print(f"{i + 1}: {order}")
    else:
        print("No orders found.")

def order_statuses(order_status):
     print("----Order status----")
     if order_status:
        for i, status in enumerate(order_status):
                print(f"{i + 1}: {status}")

def add_order(orders, products, couriers):
    try:
      customer_name = input("Enter customer name: ")
      customer_address = input("Enter customer address: ")
      customer_phone = input("Enter customer phone: ")

      courier_list(couriers)
      courier_index = int(input("Enter courier index: ")) - 1

      product_list(products)
      items = input("Enter product index -comma-separated: ")

      courier_list(couriers)
      courier_index = int(input("Enter courier index: "))

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
      save_data(orders_file, orders)  
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Index out of range. Please try again.")

def update_order_status(orders, order_status):
    try:
        order_list(orders)
        order_index = int(input("Enter order index to update: ")) - 1

        order_statuses(order_status)
        status_index = int(input("Enter index to update status: ")) - 1  

        orders[order_index]['status'] = order_status[status_index]['status']
        print("Order status updated.")
        save_data(orders_file, orders)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Index out of range. Please try again.")


def update_existing_order(orders):
    try:
        order_list(orders)
        index = int(input("Enter order index to update: ")) - 1
        
        order = orders[index]
        for key in order:
            updated_order = input(f"Enter new {key} (or leave blank to keep current '{order[key]}'): ")
            if updated_order:
                order[key] = updated_order
                print("Order updated.")
                save_data(orders_file,orders) 
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Index out of range. Please try again.")

def delete_order(orders):
    try:
        order_list(orders)
        index = int(input("Order index to delete: ")) - 1
        orders.pop(index)
        print("Order has been  has been deleted.")
        save_data(orders_file,orders)          
    except ValueError:
        print("Invalid input format. Please enter a number.")
    except IndexError:
        print("Index out of range. Please try again.")
        
 # Main function to start the management systems

def main():
    while True:
        print("----Main Menu----")
        print("1. Product Management System")
        print("2. Courier Management System")
        print("3. Order Management System")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_management_system(products)
        elif choice == '2':
            courier_management_system(couriers)
        elif choice == '3':
            order_management_system(orders, products, couriers, order_status)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Load data from CSV files
    products = load_data(products_file)
    couriers = load_data(couriers_file)
    orders = load_data(orders_file)
    order_status = load_data(orders_status_file)

    main()   