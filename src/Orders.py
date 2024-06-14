import os
import pymysql
from dotenv import load_dotenv
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

def order_inventory():
    print("----Order Catalogue----")
    print("1. Order List")
    print("2. Add an Order")
    print("3. Update Existing Order Status")
    print("4. Update Existing Order")
    print("5. Delete")
    print("0. Return to Main Menu")

def order_list():
    orders = fetch_query("SELECT * FROM orders")
    if orders:
        print("---Order List---")
        for order in orders:
            print(f"{order['id']}: {order}")
    else:
            print("No orders found.")
  
def order_statuses():
    order_status = fetch_query("SELECT * FROM order_status")
    if order_status:
        print("----Order statuses----")
        for status in order_status:
            print(f"{status['id']}: {status['status']}")
    else:
        print("No orders found.")

def add_order():
        customer_name = input("Enter customer name: ")
        customer_address = input("Enter customer address: ")
        customer_phone = input("Enter customer phone: ")

        Products.products_list()
        items = input("Enter product IDs -comma-separated: ")

        Couriers.courier_list()
        courier_id = int(input("Enter courier ID: "))

        status_id = 1  #  1 is 'preparing'
        execute_query("INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, status, items) VALUES (%s, %s, %s, %s, %s, %s)",
                (customer_name, customer_address, customer_phone, courier_id, status_id, items))
        print("Order added.")
    
def update_order_status():
    try:
        order_list()
        order_id = int(input("Enter order ID to update status: "))

        order_statuses()
       # status_id = int(input("Enter new status ID: "))
        status_id_name = input("Enter delivery status:")

        execute_query("UPDATE orders SET status = %s WHERE id = %s", (status_id_name, order_id))
        print("Order status updated.")
    except ValueError:
        print("Invalid input.")      
    except pymysql.MySQLError as e:
            print(f"Error updating order status: {e}")

def update_existing_order():
    try:
        order_list()
        order_id = int(input("Enter order ID to update: "))
        customer_name = input("Enter new customer name or leave blank to keep current): ")
        customer_address = input("Enter new customer address or leave blank to keep current): ")
        customer_phone = input("Enter new customer phone or leave blank to keep current): ")

        Products.products_list()
        items = input("Enter new product IDs - comma-separated, leave blank to keep current): ")

        Couriers.courier_list()
        courier_id = input("Enter new courier_id (leave blank to keep current): ")
       
        order_statuses()
       # status_id = int(input("Enter new status ID: "))
        status_id_name = input("Enter delivery status:")

        if customer_name:
            execute_query("UPDATE orders SET customer_name = %s WHERE id = %s", (customer_name, order_id))
        if customer_address:
            execute_query("UPDATE orders SET customer_address = %s WHERE id = %s", (customer_address, order_id))
        if customer_phone:
            execute_query("UPDATE orders SET customer_phone = %s WHERE id = %s", (customer_phone, order_id))
        if items:
            execute_query("UPDATE orders SET items = %s WHERE id = %s", (items, order_id))
        if courier_id:
            execute_query("UPDATE orders SET courier_id = %s WHERE id = %s", (int(courier_id), order_id))
        if status_id_name:
                  execute_query("UPDATE orders SET status = %s WHERE id = %s", (status_id_name, order_id))
        print("Order updated.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error updating order: {e}")

def delete_order():
    try:
        order_list()
        order_id = int(input("Enter order ID to delete: "))
        execute_query("DELETE FROM orders WHERE id = %s", (order_id,))
        print("Order deleted.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error deleting order: {e}")

# Main program loop
if __name__ == "__main__":
    try:
        while True:
            order_inventory()
            order_choice = input("Enter choice: ")
            if order_choice == '1':
                order_list()
            elif order_choice == '2':
                add_order()
            elif order_choice == '3':
                update_order_status()
            elif order_choice == '4':
                update_existing_order()
            elif order_choice == '5':
                delete_order()
            elif order_choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        try:
            connection.close()
            print("Database connection closed.")
        except pymysql.MySQLError as e:
            print(f"Error closing connection: {e}")
