#!/usr/bin/env python3
import argparse
from core import Calculator

def main():
    parser = argparse.ArgumentParser(description="Your Cli Tool")
    parser.add_argument("operation", choices=["+", "-", "x", "/", "xx"])
    parser.add_argument("numbers", nargs="+", type= float, help="Numbers To Work On")
    args = parser.parse_args()

    calculator = Calculator(*args.numbers)

    if args.operation == "+":
        print(f"Result of Sum: {calculator.add()}")
    elif args.operation == "-":
        print(f"Result of Subtraction: {calculator.subtract()}")
    elif args.operation == "x":
        print(f"Result of Multiplication: {calculator.multiply()}")
    elif args.operation == "xx":
        print(f"Result of Exponentiation: {calculator.exponentiation()}")
    elif args.operation == "/":
        counter = 0
        for number in range(1,len(args.numbers)):
            if args.numbers[number] == 0:
                counter+= 1
                print("ERROR! DIVISION BY ZERO DETECTED! PLEASE TRY AGAIN")
        if counter== 0:
            print(f"Result of Division: {calculator.divide()}")


if __name__ == "__main__":
    main()

