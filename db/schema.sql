CREATE DATABASE IF NOT EXISTS Mini_Project;
USE Mini_Project;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS couriers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    courier_id INT,
    status VARCHAR(50) NOT NULL,
    items TEXT NOT NULL,
    FOREIGN KEY (courier_id) REFERENCES couriers(id)
   
);

CREATE TABLE order_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(50) NOT NULL
);

INSERT INTO products (name, price) VALUES ('Cherry Berry', 2.99);
INSERT INTO products (name, price) VALUES ('Savory Surprise', 3.49);
INSERT INTO products (name, price) VALUES ('Strawberry Peach', 4.99);
INSERT INTO products (name, price) VALUES ('Coconut Lime', 3.99);
INSERT INTO products (name, price) VALUES ('Vanilla Chai', 2.49);
INSERT INTO products (name, price) VALUES ('Cola Pinada', 3.89);
INSERT INTO products (name, price) VALUES ('Banana Ice-cream', 2.99);



INSERT INTO couriers (name, phone) VALUES ('Dash Door', '123-456-7890');
INSERT INTO couriers (name, phone) VALUES ('Deliveroo', '234-567-8901');
INSERT INTO couriers (name, phone) VALUES ('Just Eats', '345-678-9012');
INSERT INTO couriers (name, phone) VALUES ('Uber Eats', '123-345-345');


INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, status, items) 
VALUES ('John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 'preparing', '2,3,4');



INSERT INTO order_status (status) VALUES
('preparing'),
('out for delivery'),
('delivered');