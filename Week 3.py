
# Order Menu
orders = [{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}]

order_status = ["Preparing", "Out for delivery", "Delivered"]

couriers = ["Uber Eats", "Deliveroo", "Just Eats"]

def order_inventory():
    print("\nOrder Catalogue")
    print("1. View")
    print("2. Add ")
    print("3. Update Existing Status")
    print("4, Update Existing Order")
    print("5. Delete")
    print("0. Return to Main Menu")

def order_system(orders):
    while True:
        order_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # view orders list
            print("Orders")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
                exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
                if exit_choice == 'e':
                    exit()

        elif choice == '2':
            # add/ take customer orders - print courier lists for order
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            customer_phone = input("Enter customer phone: ")
            print("Couriers:")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")
            courier_index = int(input("Enter courier index: ")) -1
            order = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "courier": courier_index,
                "status": "preparing"
            }
            orders.append(order)
            print("Order added.")

        elif choice == '3':
            # update an existing order status
            print("Orders:")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            index = int(input("Order index to update status: "))-1
            print("Order status:")
            for i, status in enumerate(order_status):
                print(f"{i + 1}: {status}")
            status_index = int(input("Enter status index: ")) -1
            orders[index]['status'] = order_status[status_index]
            print("Order status updated.")

        elif choice == '4':
            # stretch update existing order
            print("Orders:")
            for i, order in enumerate(orders):
                print(f"{i}: {order}")
            index = int(input("Enter order index to update: "))
            order = orders[index]
            for key in order:
                if key != 'status':
                    new_value = input(f"Enter new {key} (or leave blank to keep current): ")
                    if new_value:
                        order[key] = new_value
            print("Order updated.")

        elif choice == '5':
            print("Orders:")
            for i, order in enumerate(orders):
                print(f"{i + 1}: {order}")
            index = int(input("Order index to delete: ")) -1
            orders.pop(index)
            print("Order deleted.")
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    order_system(orders)