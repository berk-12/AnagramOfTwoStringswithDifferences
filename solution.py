########################################
#Author : Baran Berk Bacalan
########################################
import collections
print("NOTE!: Please type "'exit'" for quit the program.")
while(True):
    a=input("a: ")
    if(a == 'exit'):
        break
    b=input("b: ")
    if(b == 'exit' ):
        break

    listOfA = list(a)
    listOfA.sort()
    listOfB = list(b)
    listOfB.sort()
    #print("a : ",a," b : ",b)

    #print("list 1 : ",listOfA)
    #print("list 2 : ",listOfB)

    lettersOfA = {}
    counterA = 0
    for i in a:
        if(i in lettersOfA):
            lettersOfA[i] = lettersOfA[i] + 1
        else:
            lettersOfA[i] = 1

    lettersOfB = {}
    counterB = 0
    for i in b:
        if(i in lettersOfB):
            lettersOfB[i] = lettersOfB[i] + 1
        else:
            lettersOfB[i] = 1

    sortedA = collections.OrderedDict(sorted(lettersOfA.items()))
    sortedB = collections.OrderedDict(sorted(lettersOfB.items()))
    #print("A : ",sortedA)
    #print("B : ",sortedB)





    if(listOfA == listOfB):
        print("They are anagrams")
    else:
        deletionsA = 0
        deletionsB = 0

        for i in sortedA:
            if(i not in sortedB):
                deletionsA = deletionsA + sortedA[i]
            elif(sortedA[i] > sortedB[i]):
                deletionsA = deletionsA + (sortedA[i] - sortedB[i])
        for k in sortedB:
            if (k not in sortedA):
                deletionsB = deletionsB + sortedB[k]
            elif (sortedB[k] > sortedA[k]):
                deletionsB = deletionsB + (sortedB[k] - sortedA[k])

        print('remove ',deletionsA,' characters from "',a,'" and ',deletionsB,' characters from "',b,'"')
