
def exData(blist,num):
    for r in range(1,num):
        line = blist[r]
        temp = line.split(",") # "1,0,3,Braund,male" split up by comma
        print("Passenger ID: " + temp[0] + " Did " + temp[3] + " survive? " + temp[1] + " Gender: " + temp[5] + " Age: " + temp[6] + " " + temp[3] + " payed " + temp[10] + "$ for their ticket and was in Class " + temp[2])
    

# file input

fi = open("titanic.csv","r") # read only, write
biglist = fi.readlines()
fi.close()

print(len(biglist)) # len tells you #s in list
print(biglist[0]) # print column names

exData(biglist,4) # send # list up to function
