dividend = int(input("Enter a number in decimal: "))
divisor = 2
binaryNumber = ""
if dividend >= 0:
    if dividend >= divisor:
        while dividend >= divisor:
            quotient = dividend // divisor
            remainder = dividend % divisor
            dividend = quotient
            binaryNumber = str(remainder) + binaryNumber
            if dividend < divisor:
                binaryNumber = str(quotient) + binaryNumber
    else:
        binaryNumber = str(dividend)
    # Print the final result
    print("Binary Number: ", binaryNumber)
else:
    print("Please enter a number greater than 0")


