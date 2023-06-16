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

guess = input("How do you translate computer to Klingon?")
#if statement to check if guess is right or not
if guess == klingon[2]:
    print("Correct!")
else:
    print("Sorry you're wrong! \nThe correct answer is " + klingon[2] + ".")