#Website used for help wiyh join()
#https://www.programiz.com/python-programming/methods/string/join 

#constant ages
names = ["Frodo","Samwise","Gandalf","Legolas","Gimli","Aragorn","Boromir","Merry","Pippin"]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
#user input for age and name
new_name = input("Enter the charachter's name: ")
new_age = input("Enter the charachter's age: ")
#check for valid age and if invalid end the code
if int(new_age) < 0:
    print("Invalid age.")
    exit()
#create a list with the names of younger charachters
younger = []
i = 0 
while i <= len(names)-1:
    if int(new_age) > ages[i]:
        younger.append(names[i])
    i = i + 1
#use if statement to only print if the list has one name or more
if len(younger) >= 1:
    print(new_name + " is " + new_age + " years old, and they are older than " + ", ".join(younger) + ".")

#create a list with the names of older characters
older = []
a = 0
while a <= len(names)-1:
    if int(new_age) < ages[a]:
        older.append(names[a])
    a = a + 1 
#use if statement to only print if the list has one name or more
if len(older) >= 1:
    print(new_name + " is " + new_age + " years old, and they are younger than " + ", ".join(older) + ".")

    