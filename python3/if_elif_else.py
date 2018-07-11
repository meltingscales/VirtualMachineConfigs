if 5 > 0:
    x = int(input("x?"))
    y = int(input("y?"))

print("You entered '%d'" % x)
print("You entered '%03d'" % y)

if(x > y):
    print("x > y")
elif(x < y):
    print("x < y")
else:
    print("x = y")

print("%d, %d" % (x, y,))
print("{b}, {a}".format(a=x, b=y))
