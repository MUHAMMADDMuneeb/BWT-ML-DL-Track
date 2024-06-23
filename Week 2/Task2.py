def Is_even(number):
   
    if number % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter an integer: "))
result = Is_even(num)
if result == True:
     print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")