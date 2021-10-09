dict = {'Mount Everest':'8848','Lhotse':'8516','K2':'8611','Makalu':'8485','Kangchenjunga':'8586'}
print("names:")
for name in dict:
    print(name)
print("altitudes:")
for value in dict.values():
    print(value)
print("height statements:")
for name in dict:
    print(name + " is " + dict[name] + " meters tall.")