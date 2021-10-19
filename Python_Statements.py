lis = [1,2,1,3,4,5,6,4,7,4,8,9,10]
list = sorted(lis)

new = []
new.append(list[0])
for i in range (len(list)):

# To add and update list
    if i>=1:
        new.append(list [i] + new[i-1])

    
# To classify odd or ewv
    if (list[i]%2==0):
        print("Even at location %s with value %s"%((i+1),(list[i])))
    else:
        print("Odd at location %s with value %s"%((i+1),(list[i])))

print("score  is " + str(new[-1]))
print(list)
print(new)


# for-loop on dictionary
d = {'k1':1,'k2':2,'k3':3}
for i in d:
    print(d[i])


