
numList = []
primeList = []

pNum = int(input("Enter a number greater than 1: "))

for x in range(1, pNum+1):
    if x > 1:
        numList.append(x)
        for z in range(2, x):
            if(x % z) == 0:
                break
        else:
            primeList.append(x)
            print(x, "is prime")

print(numList)
print(primeList)