s = 'aabcdefg i love pie a lot!'

d = {}

for char in s: # a
  
    if char not in d: #a isn't in d, b/c d={}
        d[char] = 0 #d['a'] = 0

    d[char] += 1 # d['a'] = 0+1 = 1
    
    print('added "'+char+'". we\'ve seen it "'+str(d[char])+'" times.')
    print('d:'+str(d))
    
print(s)
print(d)

for char in 'aeiou':
  print(char, d[char])