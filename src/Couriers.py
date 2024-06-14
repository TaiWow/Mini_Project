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
    

# --------Courier Management --------
# Functions to manage Courier management
        
def display_courier_inventory():
    print("----Courier System----")
    print("1. Courier List")
    print("2. Create New Courier")
    print("3. Update Courier ")
    print("4. Delete Courier ")
    print("0. Return to Main Menu")

def courier_list():
    couriers = fetch_query("SELECT * FROM couriers")
    if couriers:
        print("---Courier List ----:")
        for courier in couriers:
            print(f"{courier['id']}: {courier['name']} - {courier['phone']}")
    else:
        print("No couriers found.")

def add_courier():
    name = input("Enter courier name: ")
    phone = input("Enter courier phone: ")
    execute_query ("INSERT INTO couriers (name, phone) VALUES (%s, %s)", (name, phone))
    print("Courier added.")

def update_courier_list():
    courier_list()
    try:
        courier_id = int(input("Enter courier ID to update: "))
        name = input("Enter new name or leave blank to keep current): ")
        phone = input("Enter new phone or leave blank to keep current): ")

        if name:
            execute_query("UPDATE couriers SET name = %s WHERE id = %s", (name, courier_id))
        if phone:
            execute_query("UPDATE couriers SET phone = %s WHERE id = %s", (phone, courier_id))
        print("Courier updated.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error updating courier: {e}")

def delete_courier():
    courier_list()
    try:
        courier_id = int(input("Enter courier ID to delete: "))
        execute_query("DELETE FROM couriers WHERE id = %s", (courier_id,))
        print("Courier deleted.")
    except ValueError:
        print("Invalid input.")
    except pymysql.MySQLError as e:
        print(f"Error deleting courier: {e}")


# --------Main Excecution Block-------

if __name__ == "__main__":
    try:
        while True:
            display_courier_inventory()
            courier_choice = input("Enter choice: ")

            if courier_choice == '1':
                courier_list()
            elif courier_choice == '2':
                add_courier()
            elif courier_choice == '3':
                update_courier_list()
            elif courier_choice == '4':
                delete_courier()
            elif courier_choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        try:
            connection.close()
            print("Database connection closed.")
        except pymysql.MySQLError as e:
            print(f"Error closing connection: {e}")
