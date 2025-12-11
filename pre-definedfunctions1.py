total = 0
password=input("What is your password: ")
for index in range(0, len(password)):
    total += ord(password[index])
remainder = str(total % 11)
new_password =password+remainder
print(new_password)
