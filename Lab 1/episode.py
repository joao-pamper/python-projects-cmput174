#reference for find(): https://www.w3schools.com/python/ref_string_find.asp

#ask for user input
ep = input("What is the name of the episode? ")
#find a reference to print the season number
season = ep.find("E")-1
#find a reference to print the episode number and name
episode = ep.find("_",4,8)
print ("Season " + str(ep[1:season]) + ", Episode " + str(ep[(season+2):episode]) + ": " + str(ep[(episode+1):]) + " (The Simpsons)")