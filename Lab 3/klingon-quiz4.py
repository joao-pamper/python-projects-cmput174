'''
This code will read the file with words in engish and klingon and ask user to 
guess a word with a specified consonant that the user can also choose
Author: Joao Pedro Amaral Pereira
When: February 3, 2023
'''
#open file and excract as a list
with open('klingon-english.txt', 'r') as file:
    text = file.readlines()

#separate text list into a list with the names in klingon and a list in english
klingon = []
english = []
i = 0
while i <= len(text) - 1:
    line = text[i]
    divider = line.find("|")
    klingon.append(line[0:divider])
    english.append(line[divider+1:len(line)-1])
    i = i + 1

#create a list with all consonants, the list also is 'paired' with the words that contain it
consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]
choice = input('Which consonant do you want to practice with? \n')

#check if consonant is valid and if not ask user to input another one until valid
a = 0
while a <= len(consonants) - 1:
    if choice == consonants[a]:
        break
    elif a == len(consonants) - 1:
        choice = input('Please enter a valid consonant. \n')
        a = 0     # to make sure that it will iterate all consonants
    else:
        a = a + 1

#create two lists with all the letters of the klingon word to use for the hints
word_hint = []
word_hint2 = []
for letter in klingon[a]:
    word_hint.append(letter)
    word_hint2.append(letter)

attempts = 3
guess = input("How do you translate " + english[a] + " to Klingon? You have " + str(attempts) + " attempts left. \n")

# while loop to control the attempts
while attempts >= 0:
    attempts = attempts - 1  
    #if statement to check if guess is right or not
    if guess == klingon[a]:
        print("Correct!")
        attempts = -1
    #if correct 
    elif attempts == 0:
        print("The correct answer is " + klingon[a] + ".")
        attempts = -1
    #for first hint
    elif attempts == 2:

        b = 1
        while b <= len(word_hint2) - 2:
            word_hint2[b] = '*'
            b = b + 1
        hint = ''
        guess = input("Sorry you're wrong! \nHow do you translate " + english[a] + " to Klingon? You have " + str(attempts) + " attempts left. \nHint: " + hint.join(word_hint2) + " \n")
    #for second hint
    elif attempts == 1:
        import random
        random_letter = random.randint(1, len(word_hint)-2)
        b = 1
        while b <= len(word_hint) - 2:
            if b == random_letter:
                b = b +1
            else:
                word_hint[b] = '*'
                b = b + 1        
        hint = ''
        guess = input("Sorry you're wrong! \nHow do you translate " + english[a] + " to Klingon? You have " + str(attempts) + " attempts left. \nHint: " + hint.join(word_hint) + " \n")
    