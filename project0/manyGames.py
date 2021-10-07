l = ["uno","soccer","tennis","hearts"]
print("I like to play" , *l)
cont = True
while (cont == True):
    l.append(input("What game do you like?"))
    contin = input("Any others? (yes or no)")
    if (contin == "yes"):
        cont = True
    else:
        cont = False
print("We like to play" , *l)