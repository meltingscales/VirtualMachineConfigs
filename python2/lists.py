def item(l, idx):
    print("lst["+str(idx)+"] aka "+str(idx)+"th item in list: "+str(l[idx]))
    return l[idx]

#     0  1  2  3  4  5  6     7       8    9
l1 = [1, 2, 3, 4, 5, 6, 7, 'eight', [1,2], 10]

print("A beautiful list:")
print(l1)

print("L1 is "+str(len(l1))+" items long")

item(l1,0) #l1[0]
print(l1[0])

print(l1[5])

# Note these are the same item!
item(l1, len(l1)-1) # l1[len(l1)-1]
item(l1, -1) #l1[-1]


# C
#for(int i = 0; i < 10; i++)

#using indices to index the list
for i in range(len(l1)):
    item(l1, i)

    if i == 5:
        print("FIFTH ITEM, WOO!")

#using iteration on the list itself
for thing in l1:
    print(thing)


numbers = range(1, 10, 2)
print(numbers)

numbers = range(len(l1)) #same as range(0, 10, 1)
print(numbers)

print(l1[0:2])

print(":-1")
print(l1[:-1])

print("::-1")
print(l1[::-1])

print(":")
print(l1[:])

print(":3")
print(l1[:3])

      #start : stop : skip
print("::3")
print(l1[::3])

print("1::2")
print(l1[1::2])

print("-1::-2")
print(l1[-1::-2])
