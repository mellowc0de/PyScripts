animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals: 
  chars += len(animal)

print("Total characters: {} | Average length: {}".format(chars, chars/len(animals)))
for index, animal in enumerate(animals):
  print("{} - {}".format(index + 1, animal))

print("----------------------------------------------")
# Enumerate a list
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))