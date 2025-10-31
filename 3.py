PetPurchased = ["Dog","Dog","Cat","Rabbit","Hamster","Cat","Hamster", "Budgie"]
last_user = 0
target_value = "Budgie"
for index in range(len(PetPurchased)):
    if target_value == PetPurchased[index]:
        last_user = index+1
print(last_user)
