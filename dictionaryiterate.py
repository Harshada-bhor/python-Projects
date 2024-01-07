#Demonstration of dictionary

print("Demonstration of dictionary")

#data : heterogenious
#ordered : yes
#indexed : no
#mutable : yes
#duplicates : no


#programming = {"c": "ritchi","c++":"stroupstup", "java":"gosling","python":"rossum"}
batches = {"ppa":18000,"lb":16700,"python":16500,"angular":15000}

print("data of dictionary :",batches)

print("data traversal using the loop")

for x in batches:
    print(x)
print("                                ")

print("data traversal using the loop")

for x in batches:
    print(x,batches.get(x))
print("                                ")

print("data traversal using the loop")

for x in batches:
    print(x,batches[x])
print("                                ")


keybatches = batches.keys()
print(type(keybatches))
print(keybatches)

valuebatches = batches.values()
print(type(valuebatches))
print(valuebatches)
























