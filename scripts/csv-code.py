
import csv
# product csv 
products = [
    {"name": "Cherry Berry", "price": 2.99},
    {"name": "Savory Surprise", "price": 3.49},
    {"name": "Strawberry Peach", "price": 4.99},
    {"name": "Coconut Lime", "price": 3.99},
    {"name": "Vanilla Chai", "price": 2.49}]

with open('products.csv', 'w', newline='') as product_file:
  writer = csv.DictWriter(product_file, fieldnames=["name", "price"])
  writer.writeheader()
  writer.writerows(products)


# orders csv 
orders = [{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing",
  "items": "2,3,4"
}]

with open('orders.csv', 'w', newline='') as order_file:
  writer = csv.DictWriter(order_file, fieldnames=["customer_name", "customer_address", "customer_phone", "courier", "status","items"])
  writer.writeheader()
  writer.writerows(orders)


# couriers csv 
couriers = [
    {"name": "Uber Eats", "phone": "123-456-7890"},
    {"name": "Deliveroo", "phone": "234-567-8901"},
    {"name": "Just Eats", "phone": "345-678-9012"}]

with open('couriers.csv', 'w', newline='') as courier_file:
  writer = csv.DictWriter(courier_file, fieldnames=["name", "phone"])
  writer.writeheader()
  writer.writerows(couriers)


# order status csv 
order_status = ["Preparing", "Out for delivery", "Delivered"]

with open('order_status.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(order_status)



products = ["Cherry Berry", "Savory Surprise", "Strawberry Peach", "Coconut Lime", "Vanilla Chai"]

# Open the file in write mode with a context manager
with open("products.txt", "w") as file:
  # Loop through each product name with index
  for index, product in enumerate(products, start=1):
    # Write the index and product name with formatting
    file.write(f"{index}. {product}\n")

print("Products written to products.txt with index!")










# order_status
order_status = ["Preparing", "Out for delivery", "Delivered"]

with open('order_status.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(order_status)
