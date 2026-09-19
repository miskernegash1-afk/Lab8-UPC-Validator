"""
Program Name: UPC Validator
Author: Misker Negash
Purpose: This program checks whether a 12-digit UPC-A code is valid.
Starter Code: No starter code was used.
Date: September 19, 2026
"""

upc = input("Enter a 12-digit UPC: ")
def find_upc(first_11):
    odd_total = 0
    even_total = 0
    for i in range(0, 11, 2):
        odd_total = odd_total + int(first_11[i])

    odd_total = odd_total * 3