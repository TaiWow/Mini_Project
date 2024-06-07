

def main_menu():
    print("\nMain Menu")
    print("1. Product")
    print("2. Couriers")
    print("3. Orders")
    print("0. Exit")

# products inventory

products = [
    {"name": "Cherry Berry", "price": 2.99},
    {"name": "Savory Surprise", "price": 3.49},
    {"name": "Strawberry Peach", "price": 4.99},
    {"name": "Coconut Lime", "price": 3.99},
    {"name": "Vanilla Chai", "price": 2.49}
]

def product_inventory():
    print("\nProduct Inventory")
    print("1. View")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("0. Return to Main Menu")

def product_inventory_management(products):
    while True:
        product_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # View product inventory
            print("Products:")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
            exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
            if exit_choice == 'e':
                exit()

        elif choice == '2':
            # Add new product to list
            product_name = input("Enter name: ")
            try:
                product_price = float(input("Enter price: "))
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue
            product = {"name": product_name, "price": product_price}
            products.append(product)
            print(f"'{product_name}' added to product list.")

        elif choice == '3':
            # Update an existing product list
            print("Products:")
            for i, product in enumerate(products):
                print(f"{i + 1}:  {product['name']},  {product['price']}")
            try:
                index = int(input("Product index to update: ")) - 1
                if index < 0 or index >= len(products):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            product = products[index]
            for key in product:
                new_product_value = input(f"Enter new {key} (or leave blank to keep current '{product[key]}'): ")
                if new_product_value:
                    product[key] = float(new_product_value) if key == 'price' else new_product_value
            print("Product has been updated.")

        elif choice == '4':
            # Delete product via index
            print("Products:")
            for i, product in enumerate(products):
                print(f"{i + 1}: {product['name']},  {product['price']}")
            try:
                index = int(input("Product index to delete: ")) - 1
                if index < 0 or index >= len(products):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            products.pop(index)
            print("Product has been deleted.")
        else:
            print("Invalid choice. Try again.")

# couriers menu

couriers = [
    {"name": "Uber Eats", "phone": "123-456-7890"},
    {"name": "Deliveroo", "phone": "234-567-8901"},
    {"name": "Just Eats", "phone": "345-678-9012"}
]

order_status = ["Preparing", "Out for delivery", "Delivered"]

def courier_inventory():
    print("\nCourier Menu")
    print("1. View")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("0. Return to Main Menu")

def courier_inventory_management(couriers):
    while True:
        courier_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # view list of current couriers
            print("Couriers:")
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
            print(f"Courier '{courier_name}' with phone '{courier_phone}' added.")

        elif choice == '3':
            # update existing courier
            print("Couriers:")
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
                new_courier = input(f"Enter new {key} (or leave blank to keep current '{courier[key]}'): ")
                if new_courier:
                    courier[key] = new_courier
            print("Courier has been updated.")

        elif choice == '4':
            # delete a courier
            print("Couriers:")
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


# Order Menu

orders = [{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing",
  "items": ["items"]
}]

order_status = ["Preparing", "Out for delivery", "Delivered"]

couriers = [
    {"name": "Uber Eats", "phone": "123-456-7890"},
    {"name": "Deliveroo", "phone": "234-567-8901"},
    {"name": "Just Eats", "phone": "345-678-9012"}
]

products = [
    {"name": "Cherry Berry", "price": 2.99},
    {"name": "Savory Surprise", "price": 3.49},
    {"name": "Strawberry Peach", "price": 4.99},
    {"name": "Coconut Lime", "price": 3.99},
    {"name": "Vanilla Chai", "price": 2.49}
]

def order_inventory():
    print("\nOrder Catalogue")
    print("1. View")
    print("2. Add")
    print("3. Update Existing Status")
    print("4. Update Existing Order")
    print("5. Delete")
    print("0. Return to Main Menu")

def order_system(orders):
    while True:
        order_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # View orders list
            print("Orders:")
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
            print("Products:")
            for i, product in enumerate(products):
                print(f"{i + 1}: {product['name']} at ${product['price']}")
            items = input("Enter product indexes (comma-separated): ")
            items = [int(x) - 1 for x in items.split(",")]
            print("Couriers:")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")
            courier_index = int(input("Enter courier index: ")) - 1
            order = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "courier": courier_index,
                "status": "preparing",
                "items": items
            }
            orders.append(order)
            print("Order added.")

        elif choice == '3':
            # Update an existing order status
            print("Orders:")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            try:
                index = int(input("Order index to update status: ")) - 1
                if index < 0 or index >= len(orders):
                    print("Invalid index. Please try again.")
                    continue
            except ValueError:
                print("Invalid. Please enter a number.")
                continue
            print("Order status:")
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
            print("Orders:")
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
                new_value = input(f"Enter new {key} (or leave blank to keep current '{order[key]}'): ")
                if new_value:
                    order[key] = new_value if key != 'courier' else int(new_value) - 1
            print("Order updated.")

        elif choice == '5':
            # Delete an order
            print("Orders:")
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




if __name__ == "__main__":
    while True:
        main_menu()
        options = input("Enter options: ")
        if options == '1':
            product_inventory_management(products)
        elif options == '2':
            courier_inventory_management(couriers)
        elif options == '3':
            order_system(orders)
        elif options == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
