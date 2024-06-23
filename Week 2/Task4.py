def find_max_min(numbers_list):
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    return max_number, min_number




numbers_list = []
for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers_list.append(number)
    
    # Find and display the maximum and minimum numbers
max_number, min_number = find_max_min(numbers_list)
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")