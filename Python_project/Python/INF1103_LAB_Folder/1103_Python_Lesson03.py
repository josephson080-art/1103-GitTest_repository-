import random as rd
def dispence_drink(drink):
    drinksnum = [0,0,0]  # [Coke, Water, Juice]
    if drink.strip().lower() == "coke":
        print(f"Dispensing {drink}")
        drinksnum[0] += 1
    elif drink.strip().lower() == "water":
        print(f"Dispensing {drink}")
        drinksnum[1] += 1
    elif drink.strip().lower() == "juice":
        print(f"Dispensing {drink}")
        drinksnum[2] += 1
    else:
        print(f"{drink} is not available. Please choose from Coke, Water, or Juice.")
    return drinksnum
def menu():
    print("=== Drink Dispenser Menu ===")
    print("Available drinks: Coke, Water, Juice")
    print("Type 'exit' to quit.")
def drinkstorage():
    drinkstorage = [rd.randint(0,10), rd.randint(0,10), rd.randint(0,10)]
    return drinkstorage 
def main():
    continueloopdrinks = True
    drinkstorage = drinkstorage()
    print(f"Initial drink storage: Coke: {drinkstorage[0]}, Water: {drinkstorage[1]}, Juice: {drinkstorage[2]}")
    while continueloopdrinks:
        menu()
        drink = input("Enter the drink you want:") 
        drinksnum = dispence_drink(drink)

        if drink == "exit":
            print("Thanks for using the drink dispenser. Goodbye!")
            continueloopdrinks = False
main()