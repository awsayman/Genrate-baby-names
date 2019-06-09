import random
import string
from sys import argv
scipt, filename = argv

letter_input1 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input2 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input3 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')

vowels = 'aeiouy'
constants = 'bcdfghjklmnpqrvestwxz'
letter = string.ascii_lowercase

# the following list can be modifiyed to add more letter names or less up to you

def gen():
    if letter_input1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input1 == "c":
        letter1 = random.choice(constants)
    elif letter_input1 == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input1

    if letter_input2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input2 == "c":
        letter2 = random.choice(constants)
    elif letter_input2 == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input2

    if letter_input3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input3 == "c":
        letter3 = random.choice(constants)
    elif letter_input3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input3

    name1 = letter1 + letter2 + letter3
    name2 = letter1 + letter3 + letter2
    name3 = letter2 + letter1 + letter3
    name4 = letter2 + letter3 + letter1
    name5 = letter3 + letter2 + letter1
    name6 = letter3 + letter1 + letter2
    return name1, name2, name3, name4, name5, name6
    name1, name2, name3, name4, name5, name6 = gen()


print(gen())

print("Opening file .... to write names in it")
target= open(filename, 'w')
line1 = gen()

print ("now I will New Baby Names write these files.")
target.write(str(gen()))

print ("and finally, we can close it ")
target.close()

# cridts to some youtube video that i forgot lol. thanks
