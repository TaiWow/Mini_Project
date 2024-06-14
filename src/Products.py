import os
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection details
host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")
port_number = int(os.environ.get("mysql_port", 3306))

# script to create and return database connection

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


# --------Product Management --------
# Functions to manage products management

def product_management_system():
    print("----Product Management System---- ")
    print("1. Product List")
    print("2. Add New Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("0. Return to Main Menu")

def products_list():
    products = fetch_query("SELECT * FROM products")
    if products:
        print("----Products List----")
        for product in products:
            print(f"{product['id']}: {product['name']} at ${product['price']}")
    else:
        print("No couriers found.")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    execute_query("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
    print("Product added.")

def update_product_list():
    products_list()
    try:
        product_id = int(input("Enter product ID to update: "))
        name = input("Enter new name or leave blank to keep current): ")
        price = input("Enter new price  or leave blank to keep current): ")
    
        if name:
            execute_query("UPDATE products SET name = %s WHERE id = %s", (name, product_id))
        if price:
            execute_query("UPDATE products SET price = %s WHERE id = %s", (float(price), product_id))
        print("Product updated.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error updating product: {e}")
    print("Product updated.")

def delete_product():
    products_list()
    try:
        product_id = int(input("Enter product ID to delete: "))
        execute_query("DELETE FROM products WHERE id = %s", (product_id,))
        print("Product deleted.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error deleting courier: {e}")


# --------Main Excecution Block-------

if __name__ == "__main__":
    try:
        while True:
            product_management_system()
            product_choice = input("Enter choice: ")

            if product_choice == '1':
                products_list()
            elif product_choice == '2':
                add_product()
            elif product_choice == '3':
                update_product_list()
            elif product_choice == '4':
                delete_product()
            elif product_choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        try:
            connection.close()
            print("Database connection closed.")
        except pymysql.MySQLError as e:
            print(f"Error closing connection: {e}")
