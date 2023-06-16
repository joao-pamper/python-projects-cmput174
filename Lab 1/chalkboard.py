#ask for user input
phrase = input("What is the phrase? ")
repetition = int(input("How many times do you want to write it? "))
#made this operation to add a space between phrases but not in the beginning
space = " "+phrase
print(phrase + (repetition-1)*space)