#constant ages
frodo_age = 51
gollum_age = 589
#user input for age and name
new_name = input("Enter the charachter's name: ")
new_age = input("Enter the charachter's age: ")
# if chain to determine if new charachter is older or younger than frodo
if int(new_age) == frodo_age:
    print(new_name + " is " + new_age + " years old, and they are of the same age as Frodo and younger than Gollum.")
elif int(new_age) < frodo_age:
    print(new_name + " is " + new_age + " years old, and they are younger than Frodo and Gollum.")
elif (int(new_age) > frodo_age and int(new_age) < gollum_age):
    print(new_name + " is " + new_age + " years old, and they are older than Frodo but younger than Gollum.")
elif int(new_age) == gollum_age:
    print(new_name + " is " + new_age + " years old, and they are older than Frodo but the same age as Gollum.")
elif int(new_age) > gollum_age:
    print(new_name + " is " + new_age + " years old, and they are older than Frodo and Gollum.")