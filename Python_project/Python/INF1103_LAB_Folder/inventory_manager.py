import json
import re

def menu(menunumber):
    if menunumber == 1:
        print("================================")
        print("=== Inventory Management System ===")
        print("================================")
    if menunumber == 2:
        print("---------Menu----------")
        print("1. Display All Products")
        print("2.Add product")
        print("3.Update Stock")
        print("4.Search Product")
        print("5.Save Inventory")
        print("6. Exit")

def save_inventory(inventorydict):
    with open("inventory.json", "w") as file:
        json.dump(inventorydict, file)

def load_inventory():
    try:
        print("Loading inventory from file...")
        with open("inventory.json","r") as file:
            print("Inventory.Json file found sucessfully")
            print("Inventory loaded successfully.")
            return json.load(file)
        
    except FileNotFoundError:
        print("Inventory file not found. Creating a new inventory file.")
        with open("inventory.json", "w") as file:
            json.dump({}, file)
            file.close()
        with open("inventory.json", "r") as file:
            print("Inventory file created successfully.")
            return json.load(file)

def input_checker(input_value):
    if input_value.isdigit() != True:
        print("Invalid input. Please enter a valid number.")
        return "Invalid",0
    input_value = int(input_value)
    if input_value < 0 or input_value >6:
        print("Invalid input. Please enter a number between 0 and 6.")
        return "Invalid",0
    else:
        return "Valid", input_value

def get_valid_input_ProductId(product_id, inventorydict):
    while  re.match(r"P\d{3}|p\d{3}",product_id)== None or product_id in inventorydict:
                if re.match(r"P\d{3}|p\d{3}",product_id) == None:
                    print("Invalid product ID. Please enter a valid product ID (P followed by 3 digits).")
                if product_id in inventorydict:
                    print("Product ID already exists. Please enter a unique product ID.")
                product_id = input ("Enter product ID: ")
    return product_id

def get_valid_input_ProductPrice(product_price):
    try :
        product_price = float(product_price)
        product_price = "{:.2f}".format(product_price)
        return product_price
    except ValueError:
        while True:
            print("Invalid input. Please enter a valid whole number or decimal number.")
            product_price = input("Enter product price: ")
            try:
                product_price = float(product_price)
                if product_price < 0:
                    print("Invalid input. Please enter a non-negative number.")
                    continue
                else:
                    return "{:.2f}".format(product_price)
            except ValueError:
                continue

def get_valid_input_ProductQuantity(product_quantity):
    while product_quantity.isdigit() != True or int(product_quantity) < 0:
        if product_quantity.isdigit() != True:
            print("Invalid input. Please enter a valid number.")
        if int(product_quantity) < 0:
            print("Invalid input. Please enter a non-negative number.")
        product_quantity = input("Enter product quantity: ")
    return int(product_quantity)

def add_product(inventorydict):
    product_value = {}
    looper = True
    print("=== Add Product ===")
    while looper:
        product_id = get_valid_input_ProductId(input("Enter product ID: "), inventorydict)
        product_name = input("Enter product name: ")
        product_price = get_valid_input_ProductPrice(input("Enter product price: "))
        product_quantity = get_valid_input_ProductQuantity(input("Enter product quantity: "))
        product_value = {"Name": product_name, "Price": product_price, "Quantity": product_quantity}
        return product_id, product_value

def display_all(inventorydict):
    print("-----Current Inventory--------")
    print("--------------------------------")
    for i in inventorydict:
        print(f"Product ID: {i}, Name: {inventorydict[i]['Name']}, Price: {inventorydict[i]['Price']}, Quantity: {inventorydict[i]['Quantity']} \n")
    print("--------------------------------")

def main():
    menu(1)
    inventory = load_inventory()
    loophandler = True
    while loophandler:
        menu(2)
        inputmenu = input("Enter option :")
        inputstatus , inputvalue = input_checker(inputmenu)
        if inputstatus == "Valid":
            if inputvalue == 1:
                print("temp")
            elif inputvalue == 2:
                product_id, product_value = add_product(inventory)
                inventory[product_id] = product_value
                if product_id in inventory:
                    print(f"Product {product_id} added successfully.")
            elif inputvalue == 6:
                save_inventory(inventory)
                print("Inventory saved successfully. Exiting the program.")
                loophandler = False
        elif inputstatus == "Invalid":
            print("Invalid input. Please try again.")

main()