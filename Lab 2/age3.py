#constant ages
pippin_age = 29
frodo_age = 51
gollum_age = 589
awen_age = 2901
#user input for age and name
new_name = input("Enter the charachter's name: ")
new_age = input("Enter the charachter's age: ")
#check for valid age
if int(new_age) < 0:
    print("Invalid age.")
    exit()
# if chain to determine if new charachter is older than frodo, gollum, pippin, and awen
if int(new_age) > awen_age:
    print(new_name + " is " + new_age + " years old, and they are older than Arwen, Gollum, Frodo, Pippin.")
elif int(new_age) > gollum_age:
    print(new_name + " is " + new_age + " years old, and they are older than Gollum, Frodo, Pippin.")
elif int(new_age) > frodo_age:
    print(new_name + " is " + new_age + " years old, and they are older than Frodo, Pippin.")
elif int(new_age) > pippin_age:
    print(new_name + " is " + new_age + " years old, and they are older than Pippin.")
    
    
# if chain to determine if new charachter is younger than frodo, gollum, pippin, and awen
if int(new_age) < pippin_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
elif int(new_age) < frodo_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Arwen, Gollum, Frodo.")
elif int(new_age) < gollum_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Arwen, Gollum.")
elif int(new_age) < awen_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Arwen.")
    
