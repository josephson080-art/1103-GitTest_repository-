def menuscreen():
    print("=== Inventory Auditor ===")
def main():
    inventoryvalue = 0 
    rejectnum = 0
    continue_audit = True
    while continue_audit:
        menuscreen()
        inputvalue = input("Enter the inventory value (or type 'exit' to quit): ")
        if inputvalue.lower() == 'exit':
            print("Total Units processed: ", inventoryvalue)
            print("Total Failed/rejected entries: ", rejectnum)
            continue_audit = False
        elif inputvalue.isdigit()==False:
                    print("Invalid input. Please enter a valid non integer.")
                    rejectnum += 1
        elif inventoryvalue > 500 or inventoryvalue + int(inputvalue) > 500:
            print("Inventory value exceeds the maximum limit of 500 units , please try again later or check the value again. ")
            rejectnum += 1
            print("Total Units processed: ", inventoryvalue)
            print("Total Failed/rejected entries: ", rejectnum)
            continue_audit = False
        elif int(inputvalue) < 0:
            print("Invalid input. Please enter a valid non negative integer.")
            rejectnum += 1
        else:
            inventoryvalue += int(inputvalue)
            print(f"Current inventory value: {inventoryvalue}")
main()