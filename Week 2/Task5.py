def get_student_details():
    students = []
    for i in range(3):
        print(f"Enter details for student {i+1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        students.append((name, age, grade))
    return students

def convert_to_dict(students_list):
    
    students_dict = {}
    for student in students_list:
        name, age, grade = student
        students_dict[name] = (age, grade)
    return students_dict

def display_student_details(students_dict):
    print("\nStudent Details:")
    for name, (age, grade) in students_dict.items():
     print(f"Name: {name}, Age: {age}, Grade: {grade}")


    # Get student details
students_list = get_student_details()
    
    # Convert list of tuples to dictionary
students_dict = convert_to_dict(students_list)
    
    # Display student details
display_student_details(students_dict)
