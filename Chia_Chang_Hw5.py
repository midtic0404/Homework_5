#!usr/bin/env python3
import sys


pin = "1234"

def GetInput():
    print("Enter your pin: ")
    uPin = input()

    if(len(uPin) != 4):
        print("Wrong Length")
    else:
        print("Good format")
    
    return uPin



count = 0
while (count < 3):
    print("Hi")
    count  += 1






def main():
    pass

if __name__ == "__main__":
    main()
