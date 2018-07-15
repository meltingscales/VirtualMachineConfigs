import sqlite3
from datetime import datetime, date

try:
    raw_input
except NameError:
    raw_input = input

c = sqlite3.connect('keto_tracker.db')

def create_table(c):
    c.execute('''CREATE TABLE food_log
                (id         INTEGER PRIMARY KEY,
                timeofday   DATE,
                nutgroup    TEXT,
                grams       FLOAT) ''')

try:
    create_table(c)
except sqlite3.OperationalError:
    pass #table already exists


class food_log:
    def __init__(self, tod, ng, g):
        self.timeofday = tod
        self.nutgroup = ng
        self.grams = g

    def insert_into_db(self, connection):
        connection.execute('''INSERT INTO food_log(timeofday, nutgroup, grams)
                    VALUES(?, ?, ?)''',
                    (self.timeofday, self.nutgroup, self.grams))

        connection.commit()

def logs_from_today(c):
    sql = '''SELECT * FROM food_log WHERE timeofday >= DATE('now','0 day')'''
    results = c.execute(sql)
    return [item for item in results]

choices = {
    0: 'quit',
    1: 'breakfast',
    2: 'snack',
    3: 'lunch',
    4: 'dinner',
}

for key, value in choices.items():
    if key == 0:
        print("{} will quit.".format(key))
    else:
        print("{}. Enter {} carbs".format(key, value))

askuser = raw_input("Please select a choice? :")
choice = int(askuser)

if choice == 0:
    exit()

if choice in choices.keys(): #they enter a valid choice

    carbs = int(raw_input('How many carbs did you eat for {}?\n > '.format(
        choices[choice]
    )))
    # here
    # carbs
    # choice
    # - nutgroup

    fl = food_log(datetime.now(), choices[choice], carbs)
    fl.insert_into_db(c)


#
def insert_number(c, n):
    c.execute('INSERT INTO fave_number(num) VALUES(?)', (x,))
    c.commit()

    for row in c.execute('SELECT * FROM fave_number'):
        print(row)

for item in logs_from_today(c):
    print(item)