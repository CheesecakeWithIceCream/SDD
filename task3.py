name = []
mark = []


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
        print(name[index], "scored", mark[index])

for index in range(5):
    name.append(get_name())
    mark.append(get_test_mark())
display_all(name,mark)