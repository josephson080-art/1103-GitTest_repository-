def menuscreen():
    print("=== Inventory Auditor ===")


def get_valid_input_ProductName():
    inputvalue = input("Enter Product Name (or type 'exit' to quit): ")

    if inputvalue.lower() == "exit":
        return "exit"

    if inputvalue.strip() == "":
        print("Invalid input. Product name cannot be empty.")
        return "invalid"

    return inputvalue.strip()


def get_valid_input_Quantiy():
    inputvalue = input("Enter the Quantity value (or type 'exit' to quit): ")

    if inputvalue.lower() == "exit":
        return "exit"

    try:
        return int(inputvalue)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return "invalid"


def process_delivery(current_total, new_value):
    if new_value < 0:
        print("Invalid input. Please enter a valid non-negative integer.")
        return current_total, "invalid"

    if current_total + new_value > 500:
        print("Inventory value exceeds the maximum limit of 500 units.")
        return current_total, "exceed"

    return current_total + new_value, "valid"


def generate_report(totalunit, totalreject):
    print("=== Audit Report ===")
    print(f"Total Units processed: {totalunit}")
    print(f"Total Failed/rejected entries: {totalreject}")
    print("=== End of Report ===")


def calculate_tax_amount(amount):
    tax_rate = 0.1
    return amount * tax_rate


def open_inventory():
    try:
        with open("Orders.txt", "r") as file:
            orders = file.readlines()
    except FileNotFoundError:
        with open("Orders.txt", "w") as file:
            orders = []

    return orders


def save_inventory(inventorylist):
    with open("Orders.txt", "w") as file:
        file.writelines(inventorylist)


def openreport(inventorylist):
    print("Current Orders:\n")

    if not inventorylist:
        print("There is nothing inside the list.")
        return

    for order in inventorylist:
        print(order.strip())


def determindid(inventorylist):
    if not inventorylist:
        return 1001

    order_ids = []

    for order in inventorylist:
        try:
            order_id = int(order.split(",")[0])
            order_ids.append(order_id)
        except ValueError:
            continue

    if not order_ids:
        return 1001

    return max(order_ids) + 1


def get_total_inventory(inventorylist):
    total = 0

    for order in inventorylist:
        try:
            quantity = int(order.split(",")[2])
            total += quantity
        except (ValueError, IndexError):
            continue

    return total


def checkthroughlist(inventorylist, name, amount):
    for index, order in enumerate(inventorylist):
        order_parts = order.strip().split(",")

        if len(order_parts) >= 3:
            product_name = order_parts[1].strip()

            if product_name.lower() == name.lower():
                current_quantity = int(order_parts[2].strip())
                new_quantity = current_quantity + amount

                inventorylist[index] = (
                    f"{order_parts[0]},{product_name},{new_quantity}\n"
                )

                save_inventory(inventorylist)
                return True

    return False


def main():
    inventory = open_inventory()
    openreport(inventory)

    current_inventory_value = get_total_inventory(inventory)
    rejectnum = 0
    continue_audit = True

    while continue_audit:
        menuscreen()

        inputvalueproduct = get_valid_input_ProductName()

        if inputvalueproduct == "exit":
            break

        if inputvalueproduct == "invalid":
            rejectnum += 1
            continue

        inputvalueQuantity = get_valid_input_Quantiy()

        if inputvalueQuantity == "exit":
            break

        if inputvalueQuantity == "invalid":
            rejectnum += 1
            continue

        temporary_value, errormessage = process_delivery(
            current_inventory_value,
            inputvalueQuantity
        )

        if errormessage != "valid":
            rejectnum += 1
            continue

        taxamount = calculate_tax_amount(inputvalueQuantity)

        if checkthroughlist(
            inventory,
            inputvalueproduct,
            inputvalueQuantity
        ):
            print("\nExisting order updated.")
        else:
            id = determindid(inventory)
            productstring = (
                f"{id},{inputvalueproduct},{inputvalueQuantity}\n"
            )

            inventory.append(productstring)
            save_inventory(inventory)

            print("\nNew Order Added:")
            print(productstring.strip())

        current_inventory_value = temporary_value

        print(f"Current inventory value: {current_inventory_value}")
        print(f"Tax amount for this transaction: ${taxamount:.2f}")
        print("Order successfully saved to Orders.txt\n")

    generate_report(current_inventory_value, rejectnum)


main()