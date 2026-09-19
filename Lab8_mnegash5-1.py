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