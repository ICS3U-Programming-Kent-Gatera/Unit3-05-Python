#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.13.22
# This program checks the month using numbers 1-12.


# month_match will match number 1-12 with their corresponding month.
def month_match():
    # month_user covers 0-12 and goes according to the month.
    month_user = input("What is the number of the month?: ")
    match (month_user):
        case "1":
            print("January")
        case "2":
            print("February")
        case "3":
            print("March")
        case "4":
            print("April")
        case "5":
            print("May")
        case "6":
            print("June")
        case "7":
            print("July")
        case "8":
            print("August")
        case "9":
            print("September")
        case "10":
            print("October")
        case "11":
            print("November")
        case "12":
            print("December")
            # Any other number or input will trigger this.
        case _:
            print("Invalid input.")


# This just runs our program.
if __name__ == "__main__":
    month_match()
