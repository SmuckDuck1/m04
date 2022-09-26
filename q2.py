
itemDict = {
    "apple": 0.50, "banana": 0.20, "mango": 0.99, "coconut": 2.99, "Pineapple": 3.99
}

dictVal = list(itemDict.values())
dictVal.sort(reverse = True)
dictVal = dictVal [ :3]

for x in dictVal:
    for y in itemDict.keys():
        if(itemDict[y]==x):
            print(str(y)+" : "+str(itemDict[y]))
            
            



    




