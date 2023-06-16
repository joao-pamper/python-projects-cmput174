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

print(klingon)
print(english)
#create a list with all consonants, the list also is 'paired' with the words that contain it
consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]
choice = input('Which consonant do you want to practice with? ')

#check if consonant is valid and if not ask user to input another one until valid
a = 0
while a <= len(consonants) - 1:
    if choice == consonants[a]:
        break
    elif a == len(consonants) - 1:
        choice = input('Pleas enter a valid consonant. ')
        a = 0
    else:
        a = a + 1

#find a word with the chosen consonant

guess = input("How do you translate " + english[a] + " to Klingon? ")
#if statement to check if guess is right or not
if guess == klingon[a]:
    print("Correct!")
else:
    print("Sorry you're wrong! \nThe correct answer is " + klingon[a] + ".")