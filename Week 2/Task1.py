user_info = {}
name = input("Enter your name: ")
age =int( input("Enter your age: "))
email =input("Enter your email: ")
while "@" not in email or "." not in email or email.index("@") > email.index("."):
    print("email format is incorrect.")
    email =input("Enter your email: ")
favrtnumber =input("Enter your favorite number: ")
user_info["name"]=name
user_info["age"]=age
user_info["email"]=email
user_info["favorite_number"]=favrtnumber

print(f"Hello {user_info['name']}, you are {user_info['age']} years old, "
               f"your email is {user_info['email']}, and your favorite number is {user_info['favorite_number']}.")
        
    
    
