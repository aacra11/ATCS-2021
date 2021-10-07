def crowd_test(x):
    if (len(x) > 3):
        print("The room is crowded.")
l = ["Alex","Dakin","Aidan","Marvin"]
crowd_test(l)
l.remove("Aidan")
l.remove("Marvin")
crowd_test(l)