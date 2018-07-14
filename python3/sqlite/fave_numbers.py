try:
    raw_input
except NameError:
    raw_input = input
# makes raw_input available to python 3

import sqlite3

c = sqlite3.connect('fave_numbers.db')

try:
    c.execute('''CREATE TABLE fave_number
                (id INTEGER PRIMARY KEY,
                num INTEGER) ''')
except sqlite3.OperationalError: #i.e. table exists already
    pass

def insert_number(c, n):
    c.execute('INSERT INTO fave_number(num) VALUES(?)', (x,))
    c.commit()
    
    for row in c.execute('SELECT * FROM fave_number'):
        print(row)

while True:

    try:
        i = raw_input('Fave number?\n > ')
        x = int(i)
        
        insert_number(c, x)
        
    except ValueError:

        if(i.upper() == 'QUIT'):
            exit(0)
        else:
            print("That's not a number!")
            print("(QUIT) to quit.")

    
