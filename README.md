# TaiWow_Mini-Project


# Project Background

This project is designed to efficiently manage products, couriers, and orders using a command-line interface with a MySQL database for data persistence. It addresses the needs of a client operating a pop-up smoothie shop in a busy business district, providing homemade lunches and refreshments to nearby offices. The software logs and tracks orders efficiently, maintaining a collection of products and couriers, managing customer orders, and updating order statuses while ensuring data persistence and reliability.

# Client Requirements

The project required a system that could:
1. **Manage Product Inventory**: Add, update, and delete products.
2. **Manage Courier System**: Add, update, and delete couriers.
3. **Manage Orders**: Create new orders, update order statuses, and delete orders.
4. **Provide Persistent Data Storage**: Ensure data is not lost between sessions, using plaintext files, CSV format, and ultimately a database.

# Main Functionality of the Application - Database Connection 

*Product, Courier, and Order Management System*

The application connects to a MySQL database using connection details specified in environment variables.Two primary functions are used to execute queries:

- *fetch_query*: Executes `SELECT` statements and returns the results.
- *execute_query*: Executes `INSERT`, `UPDATE`, and `DELETE` statements.

The inventory system is built with separate modules for better organization and maintainability:
- `couriers.py`
- `products.py`
- `orders.py`

When you run the application, you will see the following main menu:

---- Main Menu ------
1. Product
2. Couriers
3. Orders
0. Exit

You can choose any option by entering the corresponding number:

1. Product Management: Manages product-related operations.
2. Courier inventory: Manages courier-related operations.
3. Order inventory: Manages order-related operations.
0. Exit: Exits the application.

# Requirements and Set Up
- Python 3 
- MySQL database 
- pymysql library (install with `pip install pymysql`)
- python-dotenv library (install with `pip install python-dotenv`)

 *Configure MySQL Database* 
   - Set up your MySQL database.
   - Create the necessary database, tables, and user credentials.
   - Use schema.sql file from db folder in project directory

. *Create .env File* 
   - Create a file named `.env` in the project directory.
   - Store your MySQL connection details securely.

 *Install Libraries*
   - Use `pip` to install the required Python libraries: 
   -  pymysql 
   - python-dotenv
   - use requirement.txt
   
4 *Run the Program* 
   - Execute the main script:
   - python main.py
   
*Optional Docker Setup*

 - Create a Dockerfile for your Python application.
 - Create a `docker-compose.yml`File to set up the MySQL database and your application container.
 - Update Your python application to connect to the MySQL database using PyMySQL.

# Main Functionality of the Application - CSV based App

 Same functionality as the database connections, however dat is persistd into CSV file.

*Data Handling*
- load_data -loads data from a CSV file.
- save_data - saves data to a CSV file.

*create a data directory in project*
- product.csv
- courier.csv
- orders.csv  
- order_status.csv 

 *Run the Program* 
   - Execute the main script:
   - python main.py - Week 5.py


## Project Reflection

*How did your design go about meeting the project's requirements?*
- Each week worked through the mini- project briefs to continously update and refactor code 
- Built a program that runs on CLI
- load and persisted data to both CSV and SQL database when I exit the application
- CRUD statements implement for all products, orders and courier inventory
- structuring the code with reusable functions
- try except for error handling such as value error and index error

*If you had more time, what is one thing you would improve upon?*
- implement unit tests for each function to ensure reliability.
- adding bonus features like filtering capabilities 

*What did you most enjoy implementing?*
- coding  SQL queries in python.
- writing and refactoring functions for improved efficiency.
- seeing progress in my learning through practical application in my project.





