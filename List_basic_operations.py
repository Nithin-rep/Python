data = ["My","Team","Fires""for","Life"]
print(data)
print(type(data))

# To reverse a list
new =[ ]
for p in range(1,len(data)):
    new.append(data[-p])
new.append(data[0])
print(new)
# or using key word
print(list(reversed(data)))

# To sort a list
score = ['123','345','456','678','890']
print(sorted(score, reverse = True))

