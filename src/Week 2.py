
# couriers Inventory Management

couriers = ["Uber Eats", "Deliveroo", "Just Eats"]

order_status = ["Preparing", "Out for delivery", "Delivered"]

def display_courier_inventory():
    print("----Courier System----")
    print("1. Courier List")
    print("2. Create New Courier")
    print("3. Update Courier ")
    print("4. Delete Courier ")
    print("0. Return to Main Menu")

def manage_courier_inventory(couriers):
    while True:
        display_courier_inventory()
        choice = input("Enter choice: ")
        if choice == '0':
            break

        elif choice == '1':
            # view list of current couriers
            print("----Couriers List----")
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
            # update existing courier list
            print("----Couriers List----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")

            index = int(input(" Courier index to update: ")) - 1
            update_courier = input("Enter updated courier name: ")

            couriers[index] = update_courier
            
            print(f"Courier updated to '{update_courier}'.")

        elif choice == '4':
            # delete a courier
            print("----Couriers List----")
            for i, courier in enumerate(couriers):
                print(f"{i + 1}: {courier}")

            index = int(input("Courier index to delete: ")) - 1
            couriers.pop(index)
            print("Courier has been deleted.")
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    manage_courier_inventory(couriers)




























