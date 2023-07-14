
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

k = getKidz(data)
f = getGrp(data,"female")
m = getGrp(data,"male")

fo = open("index1.html","w")
fo.write("<html>")
fo.write("<h1>Titanic Data Analysis - Women and Children First?</h1>")
fo.write("<p>This is the result of our Titanic analysis.</p>")
fo.write("<img id='titanic-pic' src='titanic.jpeg' width='500px'>")
fo.write("<br>")
fo.write("<h2>These are the findings:</h2>")
fo.write("<svg width='800' height='500'>")
fo.write("<rect width='" + str(f * 10) + "' height='100' fill='#f5a4c6'></rect>")
fo.write("<text x='25' y='30' font-size='15pt' fill='#bf4176'>Women</text>")
fo.write("<rect y='125' width='590' height='100' fill='#fae59b'></rect>")
fo.write("<text x='25' y='155' font-size='15pt' fill='#cfa717'>Children</text>")
fo.write("<rect y='250' width='190' height='100' fill='#a4caf5'></rect>")
fo.write("<text x='25' y='280' font-size='15pt' fill='#4982c4'>Men</text>")
fo.write("</svg>")
fo.write("</html>")
fo.close()

keepgoing = True
while (keepgoing == True):
    key = input("f for female, m for male, k for kids, q for quit")
    if (key == "q"):
        keepgoing = False
        print("bye")
    elif (key == "f"):
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
