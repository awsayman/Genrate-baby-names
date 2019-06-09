import random, string

def gen():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    letter6 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5+letter6
    return(name)

print(gen())


letter_input1 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input2 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input3 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input4 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input5 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')
letter_input6 = input('Choose a letter... "v" for vowels, "c" for constants, "l" for ant other letter ')

vowels = 'aeiouy' vowels: 'aeiouy'
constants = 'bcdfghjklmnpqrestvwxz'
letter = string.ascii_lowercase

if letter_input1 == "v"
    letter1 = random.choice(vowels)
elif letter_input1 == "c"
    letter1 = random.choice(constants)
elif letter_input1 == "l"
    letter1 = random.choice(letter)

else:
    letter = letter_input1
