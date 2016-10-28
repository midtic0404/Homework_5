#!usr/bin/env python3
import sys


pin = "1234"

def GetInput():
    print("Enter your pin: ")
    uPin = input()

    if(len(uPin) != 4):
        print("Invalid PIN length. Correct format is : <9876>")
    elif(not uPin.isdigit()):
        print("Invalid PIN character. Correct format is: <9876>")
    
    return uPin



count = 0
while (count < 3):
    uPin = GetInput()
    
    if uPin == pin:
        print("Your PIN is correct")
        break
    else:
        print("Your PIN is incorrect")

    count += 1


if count == 3:
    print("Your bank card is blocked")
    exit(1)


def main():
    pass

if __name__ == "__main__":
    main()
