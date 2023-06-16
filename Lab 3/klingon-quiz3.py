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
        a = 0
    else:
        a = a + 1

attempts = 3
hint = (klingon[a])[0] + (len(klingon[a])-2)*"*" + (klingon[a])[len(klingon[a])-1:len(klingon[a])]

guess = input("How do you translate " + english[a] + " to Klingon? You have " + str(attempts) + " attempts left. \n")
while attempts >= 0:
    attempts = attempts - 1
#if statement to check if guess is right or not
    if guess == klingon[a]:
        print("Correct!")
        break
    elif attempts == 0:
        print("The correct answer is " + klingon[a] + ".")
        attempts = -1
    else:
        input("Sorry you're wrong! \nHow do you translate " + english[a] + " to Klingon? You have " + str(attempts) + " attempts left. \nHint: " + hint + " \n")
        