import sympy as sp
import os
from time import sleep

def dx_func():
    
    x = sp.Symbol('x')                                              # Define the variable of differentiation
    fx = input("Enter the function you want to differentiate: ")    # Prompt user to input function to differentiate
    fx_simpify = sp.sympify(fx)                                     # Convert string to sympy expression
    dx = sp.diff(fx_simpify, x)                                     # Differentiate the function 
    return fx,dx                                                    # Return the output/derivative

def main():
    while True:
        os.system('cls')
        print("[1] Algebraic Functions")
        print("[2] Transcendental Functions")
        print("[3] Exit Calculator")
        ch = input("\n Enter your Choice:   ")
        if ch == '1':
            fx, dx = dx_func()
            print(f"\nThe derivative of {fx} is {dx}")
            os.system('pause')
        elif ch == '2':
            fx, dx = dx_func()
            print(f"\nThe derivative of {fx} is {dx}")
            os.system('pause')
        elif ch == '3':
            print("See you again!!")
            sleep(3)
            os.system('cls')
            break
        else:
            pass

if __name__ == "__main__":
    main()