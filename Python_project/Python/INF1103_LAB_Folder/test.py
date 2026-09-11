def binary_to_decimal(binary):
    decimal = 0
    count = 0
    for digit in reversed(binary):
        if digit == "1":
            decimal += pow(2, count)
        elif digit != "0":
            print("Invalid binary number.")
            return
        count += 1
    return decimal

def binary_to_hexadecimal(binary):
    decimal = 0
    binarycombinner = ""
    hexadecimal = ""
    holdinglist = []
    for digit in binary:
        binarycombinner += str(digit)
        if len(binarycombinner) == 4:
            decimal = binary_to_decimal(binarycombinner)
            holdinglist.append(decimal)
            binarycombinner = ""
    for decimal_value in holdinglist:
        if decimal_value < 10:
            hexadecimal += str(decimal_value)
        elif decimal_value == 10:
            hexadecimal += "A"
        elif decimal_value == 11:
            hexadecimal += "B"
        elif decimal_value == 12:
            hexadecimal += "C"
        elif decimal_value == 13:
            hexadecimal += "D"
        elif decimal_value == 14:
            hexadecimal += "E"
        elif decimal_value == 15:
            hexadecimal += "F"
    hexadecimal = "0x" + hexadecimal
    return hexadecimal

def main():
    decimal = 0
    binary = input("Enter a binary number: ")
    bits = len(binary)
    decimal = binary_to_hexadecimal(binary)
    print(decimal,binary, "has", bits, "bits.")
main()
