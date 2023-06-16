#constant age
frodo_age = 51
#user input for age and name
new_name = input("Enter the charachter's name: ")
new_age = input("Enter the charachter's age: ")
# if chain to determine if new charachter is older or younger than frodo
if int(new_age) == frodo_age:
    print(new_name + " is " + new_age + " years old, and they are of the same age as Frodo.")
elif int(new_age) < frodo_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Frodo.")
elif int(new_age) > frodo_age:
    print(new_name + " is " + new_age + " years old, and they are older than Frodo.")