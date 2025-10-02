from dataclasses import dataclass
@dataclass
class person():
    name : str = 0.0
    mark : float = 0.0
    
def get_name():
    print()
    thisName = input("Enter name: ")
    return thisName

def get_test_mark():
    print()
    thisMark = int(input("Enter test mark: "))
    while thisMark < 0 or thisMark > 100:
        print("Error")
        thisMark = int(input("Enter name: "))
    return thisMark

def display_all(Name, Mark):
    print()
    for index in range(5):
        print(people[index].name, "scored", str(people[index].mark))

people = [person(),person(),person(),person(),person(),]
for index in range(5):
    people[index].name =get_name()
    people[index].mark = (get_test_mark())
display_all(people[index].name, people[index].mark)

