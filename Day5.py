
def getKidz(data):
    # the math -> numsurv / numkidz * 100
    numkidz = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""):
            if (float(temp[6]) < 16.0):
                numkidz = numkidz + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkidz) * 100

def getGrp(data,sex):
    # the math -> numsurv / numgrp * 100
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""):
            if (temp[5] == sex):
                numgrp = numgrp + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numgrp) * 100

# open titanic databas
file = open("titanic.csv","r")
cols = file.readline()
data = file.readlines()
file.close()

keepgoing = True
while (keepgoing == True):
    key = input("f for female, m for male, k for kids, q for quit")
    if (key == "q"):
        keepgoing = False
        print("bye")
    elif (key == "w"):
        g = getGrp(data,"female")
        print(round(g,1))
    elif (key == "m"):
        g = getGrp(data,"male")
        print(round(g,1))
    elif (key == "k"):
        k = getKidz(data)
        print(round(k,1))
    else:
        print("umm follow instructions please")

k = getKidz(data)
print(round(k,1))

g = getGrp(data,"female")
print(round(g,1))
