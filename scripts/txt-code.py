# couriers.txt
couriers = ["Uber Eats", "Deliveroo", "Just Eats"]

with open('couriers.txt', "w") as file:
  for index, courier in enumerate(couriers, 1):
    file.write(f"{index}. {courier}\n")
print("Couriers written to txt file.")


# order_status.txt
order_status = ["Preparing", "Out for delivery", "Delivered"]

with open('order_status.txt', "w") as file:
  for index, status in enumerate(order_status, 1):
    file.write(f"{index}. {status}\n")
print("Order status written to txt file.")


# products.txt
products = ["Cherry Berry", "Savory Surprise", "Strawberry Peach", "Coconut Lime", "Vanilla Chai"]

with open("products.txt", "w") as file:
 for index, product in enumerate(products, 1):
    file.write(f"{index}. {product}\n")
print("Products written to text file.")


#with open("products.txt", "w") as file:
  #for product in products:
    #file.write(f"{product}\n")




"""products = [
    {"name": "Cherry Berry", "price": 2.99},
    {"name": "Savory Surprise", "price": 3.49},
    {"name": "Strawberry Peach", "price": 4.99},
    {"name": "Coconut Lime", "price": 3.99},
    {"name": "Vanilla Chai", "price": 2.49}
]


header = "Name, Price\n"
with open("products.txt", "w") as file:
  file.write(header)
  for product in product:
    # Write the product name and price to the file in a formatted way
    file.write(f"{product['name']}, ${product['price']:.2f}\n")"""


