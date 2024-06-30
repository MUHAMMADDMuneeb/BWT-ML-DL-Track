# main.py
from mymath import add, subtract, multiply, divide, mod, power, sqrt

def main():
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    print(f"{a} % {b} = {mod(a, b)}")
    print(f"{a} ^ {b} = {power(a, b)}")
    print(f"sqrt({a}) = {sqrt(a):2f}")

   
if __name__ == "__main__":
    main()
