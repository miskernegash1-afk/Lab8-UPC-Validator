"""
Program Name: UPC Validator
Author: Misker Negash
Purpose: This program checks whether a 12-digit UPC-A code is valid.
Date: September 19, 2026
"""

upc = input("Enter a 12-digit UPC: ")
def find_upc(first_11):
    odd_total = 0
    even_total = 0
    for i in range(0, 11, 2):
        odd_total = odd_total + int(first_11[i])

    odd_total = odd_total * 3
# Add digits 2, 4, 6, 8, and 10
    for i in range(1, 11, 2):
        even_total = even_total + int(first_11[i])

    total = odd_total + even_total

    remainder = total % 10

    if remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - remainder

    return check_digit
# Ask the user for a UPC
while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) == 12 and upc.isdigit():
        break
    else:
        print("Error: Please enter exactly 12 digits.")


# Get the first 11 digits
first_11 = upc[:11]
# Get the last digit
provided_check_digit = int(upc[11])

print()
print(f"The first 11 digits are '{first_11}'.")
print(f"The provided check digit is '{provided_check_digit}'.")
print()

print("Calculating...")

expected_check_digit = find_upc(first_11)

print(f"The expected check digit is {expected_check_digit}.")
print()

if expected_check_digit == provided_check_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")
# Get the actual 12th digit
provided_check_digit = int(upc[11])

# Call the function
expected_check_digit = find_upc(first_11)

# Compare the returned check digit to the actual check digit
if expected_check_digit == provided_check_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")
