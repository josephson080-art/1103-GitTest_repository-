def menuscreen():
    print("=== Inventory Auditor ===")

def get_valid_input():
    inputvalue = input("Enter the inventory value (or type 'exit' to quit): ")
    if inputvalue.lower() == 'exit':
        return 'exit'
    try:
        int(inputvalue)
    except ValueError:
        print("Invalid input. Please enter a valid non-integer.")
        return "invalid"
    else:
         return int(inputvalue)
    
def process_delivery(current_total , new_value):
    if current_total > 500 or current_total + new_value > 500:
        print("Inventory value exceeds the maximum limit of 500 units , please try again later or check the value again. ")
        return 0 , "exceed"
    elif new_value < 0:
        print("Invalid input. Please enter a valid non negative integer.")
        return 0 , "invalid"
    else:
        return current_total + new_value,"Nill"

def generate_report(totalunit, totalreject):
    print("=== Audit Report ===")
    print(f'Total Units processed: {totalunit} ')
    print(f'Total Failed/rejected entries: {totalreject} ')
    print("=== End of Report ===")

def calculate_tax_amount(amount):
    tax_rate = 0.1 #10 tax rate
    tax_amount = amount * tax_rate
    return tax_amount

def open_inventory():
    orders =[]
    try:
        file = open("Orders.txt",'r')
        file.close()
    except:
        file = open("Orders.txt",'w+')
        file.close()
    finally:
        with open("Orders.txt",'r') as file:
            orders = file.readlines()
            file.close()
    return orders

def openreport(inventorylist:list):
    print("Current Orders \n")
    if not inventorylist:
        print("There is nothing inside the list ")
    for i in inventorylist:
        print(f'{i} \n')


def main():
    inventory = open_inventory()
    openreport(inventory)
    current_inventory_value = 0
    rejectnum = 0
    continue_audit = True
    while continue_audit:
        menuscreen()
        inputvalue = get_valid_input()
        if inputvalue == 'exit':
            generate_report(current_inventory_value, rejectnum)
            continue_audit = False
        elif inputvalue == "invalid" :
            rejectnum += 1 
        else:
            temporary_value,errormessage = process_delivery(current_inventory_value, inputvalue) 
            taxamount = calculate_tax_amount(inputvalue)
            if temporary_value != 0:
                current_inventory_value = temporary_value
            if errormessage == "exceed":
                rejectnum += 1
                generate_report(current_inventory_value, rejectnum)
                continue_audit = False
            if errormessage == "invalid":
                rejectnum += 1
            print(f"Current inventory value: {current_inventory_value}")
            print(f"Tax amount for this transaction: ${taxamount:.2f}")
main()