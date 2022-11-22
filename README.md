## CAFE MENU PROJECT

# Project Background
The client has launched a pop-up café in a busy business district. They
are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to
log and track orders.

# Project requirements:
I want to maintain a collection of products and couriers.
- When a customer makes a new order, I need to create this on the system.
- I need to be able to update the status of an order i.e: preparing, out-for-delivery, delivered.
- When I exit my app, I need all data to be persisted and not lost.
- When I start my app, I need to load all persisted data.
- I need to be sure my app has been tested and proven to work well.
- I need to receive regular software updates.

# How they were met:
- Program maintains a collection of:
    1. Products (Product **name** and **price**)
    2. Couriers (Courier **name** and **phone number**)
    3. Orders (Customer **name**, **address**, **phone number**, **assigned courier**, **order status** and ordered **items**)
- All data can be **updated.**
- All data is **loaded** from the database upon program start.
- All data is **saved** to the database upon program exit and when data is created/updated/removed.
- Data can optionally be **exported** from or **imported** to csv.
- A log of database transactions is **saved** into a text file.
- Application has been throughly **tested** (90+ unit tests implemented).

# Action plan for future
- Visualise data with matplotlib/jupyter.
- Refactor old code (particularly earlier tests) to be in line with recent code.

# What I enjoyed
- The problem solving aspect of figuring out how to meet project requirements within a Python program.
- Learning about unit testing while implementing it.
- That feeling when your code finally runs with no errors.

# Additional information
Author: Nathan

Cafe menu project code

- main.py: Main project
- productmenu.py: Product menu functions
- couriermenu.py: Courier menu functions
- ordermenu.py: Order menu functions
- productclass.py: Product class
- courierclass.py: Courier class
- orderclass.py: Order class
- database.py: Class that handles database interactions between menus and mySql.
- inputchecker.py: Validates list indexes
- \test: Contains unit tests.
- \data: Contains data.

### FILES THAT YOU WILL NEED TO CREATE TO RUN THIS:

- .env file with mysql host, user, pass and db variables.

Set up your database with docker-compose.yml with the following:

- table: products
columns: id, name, price
- table: couriers
columns: id, name, phone
- table: status_code
columns: id (1-4, int), status_name (Preparing, Awaiting pickup, Out for delivery, Delivered)
- table: orders
columns: id, customer_name, customer_address, customer_phone,courier (foreign key: couriers.id), statuscode (foreign key. statuscode.id), 
items (varchar)
- table: order_items
columns: order_id (foreign key: orders.id), product_id (foreign key: products.id), product_quantity