lst = '1,2,3,4,5,6,7,8'.split(',')
lst2 = '1,2,3,4,5,6,7,8'.split(',')


with open('csv_fun2.csv', 'w') as f:

	for x in lst:
		for y in lst2:
        
			thingy = ','.join([x,y])
			print(thingy)
			f.write(thingy + '\n')