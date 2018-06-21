def m(a, b):
    return a * b

def p(a, b):
    return a + b

print(1 + 2 * 3)
print(1 + (2 * 3))
print(1 + m(2,3))

print(p(   m(3,2)   ,1))
print(p(     6      ,1)) # 3 times 2 is 6
print(         7       ) # 6 plus 1 is 7


a = 'taco_bell'

b = "Burrito"

print('i like {x} at {y}'.format(x=b,y=a).title().split(' ')


x = 'tacos.txt'

print ('tacos.txt'.open())