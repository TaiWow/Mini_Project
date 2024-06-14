import os
import pymysql
from dotenv import load_dotenv
import Orders
import Products
import Couriers

# Load environment variables
load_dotenv()

# Database connection details
host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")
port_number = int(os.environ.get("mysql_port", 3306))

# Connect to the MySQL database
try:
    connection = pymysql.connect(
        host=host_name, 
        user=user_name,
        password=user_password,
        database=database_name,
        port=port_number
    )
    print("Database connection successful.")
except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

# Function to execute a query and fetch all results
def fetch_query(query, params=None):
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Error fetching query: {e}")

# Function to execute a query and commit changes
def execute_query(query, params=None):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")

def main_menu():
    print("---- Main Menu ------")
    print("1. Product")
    print("2. Couriers")
    print("3. Orders")
    print("0. Exit")

# Main program loop
if __name__ == "__main__":
    try:
        while True:
            main_menu()
            choice = input("Enter choice: ")
            
            if choice == '1':
                Products.product_management_system()
                product_choice = input("Enter choice: ")

                if product_choice == '1':
                    Products.products_list()
                elif product_choice == '2':
                    Products.add_product()
                elif product_choice == '3':
                    Products.update_product_list()
                elif product_choice == '4':
                    Products.delete_product()
                elif product_choice == '0':
                    continue
                else:
                    print("Invalid product choice. Please try again.")
            
            elif choice == '2':
                Couriers.display_courier_inventory()
                courier_choice = input("Enter choice: ")

                if courier_choice == '1':
                    Couriers.courier_list()
                elif courier_choice == '2':
                    Couriers.add_courier()
                elif courier_choice == '3':
                    Couriers.update_courier_list()
                elif courier_choice == '4':
                    Couriers.delete_courier()
                elif courier_choice == '0':
                    continue
                else:
                    print("Invalid courier choice. Please try again.")
            
            elif choice == '3':
                Orders.order_inventory()
                order_choice = input("Enter choice: ")
                
                if order_choice == '1':
                    Orders.order_list()
                elif order_choice == '2':
                    Orders.add_order()
                elif order_choice == '3':
                    Orders.update_order_status()
                elif order_choice == '4':
                    Orders.update_existing_order()
                elif order_choice == '5':
                    Orders.delete_order()
                elif order_choice == '0':
                    continue
                else:
                    print("Invalid order choice. Please try again.")
            
            elif choice == '0':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally: # ensures the connection is closed 
        try:
            connection.close()
            print("Database connection closed.")
        except pymysql.MySQLError as e:
            print(f"Error closing connection: {e}")
