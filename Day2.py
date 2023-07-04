# built in functions - round(), print()

# when using def, if you have : then indent

def getAge(age):
    cat = "baby"
    if (age <= 5):
        cat = "baby"
    elif (age > 5 and age <= 13):
        cat = "kids"
    else:
        cat = "big people"
    return cat

myage = input("enter your age as an integer (ex. 5): ")
mycat = getAge(int(myage))
print(mycat)

friends = ["neil","fiorella","elijn"]
friends.sort()
print(friends)

for f in friends: # sequential search algorithm
    if (f == "elijn"):
        print(f + " is dutch")
    else:
        print(f + " is cool")

for i in range(3):
    print(friends[i])

keepgoing = True
while (keepgoing == True):
    key = input("press q to quit: ")
    if (key == "q"):
        keepgoing = False
        print("bye")

