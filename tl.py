array = []
with open ("threeLetters.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        array = line.split(",")
chosenWord = rand(array)