Author: Nathan

Cafe menu project code

main.py: Main project

productmenu.py: Product menu functions

couriermenu.py: Courier menu functions

ordermenu.py: Order menu functions

productclass.py: Product class

courierclass.py: Courier class

orderclass.py: Order class

database.py: Class that handles database interactions between menus and mySql.

inputchecker.py: Validates list indices

FILES THAT YOU WILL NEED TO CREATE TO RUN THIS:

.env file with mysql host, user, pass and db variables.

Set up your database with docker-compose.yml with the following:

table: products, columns: id, name, price

table: couriers, columns: id, name, phone