animal = input("What animal do you want: ")
first_letter = chr(ord(animal[0])-32)
new_animal = first_letter + animal[1:]
print(new_animal)
