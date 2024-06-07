
# couriers menu

couriers = ["Uber Eats", "Deliveroo", "Just Eats"]

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
                print(f"{i + 1 }: {couriers}")
                exit_choice = input("Enter '0' to return to the main menu or 'e' to exit: ")
                if exit_choice == 'e':
                    exit()

        elif choice == '2':
            # add a new courier to list
            new_courier = input("Enter new courier: ")
            couriers.append(new_courier)
            print(f" '{new_courier}' added to courier list.")

        elif choice == '3':
            # update existing courier
            print("Couriers:")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")
            index = int(input(" Courier index to update: ")) - 1
            new_name = input("Enter updated courier name: ")
            couriers[index] = new_name
            print(f"Courier updated to '{new_name}'.")

        elif choice == '4':
            # delete a courier
            print("Couriers:")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")
            index = int(input("Courier index to delete: ")) - 1
            couriers.pop(index)
            print("Courier has been deleted.")
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    courier_inventory_management(couriers)




























