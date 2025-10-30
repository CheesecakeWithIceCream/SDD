def getTargetCharacter():
  target = input("Enter the character you are looking for")
  return target

def getCharacters():
  characters = ["Desperate Dan", "Numbskulls", "Dennis the Menace", "Minnie the Minx", "Walter", "Gnasher", "Billy Whizz"]
  return characters

def findCharacterPosition(oneToFind):
  found = False
  foundPosition = 0
  for i in range(len(characters)):
    if characters[i] == target:
      found = True
      foundPosition = i+1
      return foundPosition
    else:
      foundPosition+=1

target = getTargetCharacter()
characters = getCharacters()
foundPosition = findCharacterPosition(target)

print(findCharacterPosition(target))

# Assuming character is meant to be an element of the array