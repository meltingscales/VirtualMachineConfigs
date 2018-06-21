
user = raw_input('Diary App v9000.2\n > ')

my_file = open('file.txt', 'w')

#my_file.write('i am a FILE!')

"""
i am alive and happy
"""
# ->
"""
i
am
alive
and
happy
"""

#my_file.write(user)
# my_file.write([])

for word in user.split(' '):
    my_file.write(word+'\n')
