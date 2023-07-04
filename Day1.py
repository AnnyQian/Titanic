print("hello world")

age = 14 # this is an integer
pi = 3.14 # this is a float
name = "Anny" # this is a string
iscool = True # this is a boolean

print(age + pi)
print(age - pi)
print(age / pi)
print(age * pi)

niceoutput = round(age * pi,1)
print(niceoutput)

print(name + str(age))
print("Your name is " + name + " and your age is " + str(age))

# sequential, selection, repetition

(myage) = input("What is your age?: ") # returns a string
if(int(myage) >= 50 and int(myage) <=60):
    print("You are old")
elif(int(myage) > 60):
    print("You are a senior")
elif(int(myage) <= 19 and int(myage) >= 13):
    print("You are a teenager")
elif(int(myage) <= 12 and int(myage) >= 4):
    print("You are a child")
elif(int(myage) <=3 and int(myage) >= 1):
    print("You are a toddler")
else:
    print("You are not old congradulations")
