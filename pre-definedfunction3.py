password=input("Please enter a secure password: ")
while ord(password[0]) > 91 or ord(password[0]) > 64 and ord(password[-1]) < 35 or ord(password[-1]) > 38:
    print("First letter must be capital and last character must be $,%,&")
    password=input("Please enter a secure password ")
print("Password is secure")

