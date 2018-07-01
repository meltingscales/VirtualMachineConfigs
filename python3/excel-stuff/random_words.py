"""
Programmaticaly create an excel file that has:
 - 200 random numbers on column A
 - 200 random words from a small pool on column B(edited)
Output a new file that has:
 - All columns between 20-30 removed
 - All columns that have EXCACTLY three vowels removed
STEP 1: what is a random number?
STEP 2: How to choose a random word from a list?
STEP 3: How do I read/write .csv files?
we aint fuck with no XML right now(edited)
"""


import random
#        0    1     2     3       4      5
# words = 'i really really like chocolate cake'.split(' ')

words = ''.join(open('word_list.txt', 'r').readlines()).replace('\n\n','\n').split('\n')

print(words[0:10])

def write_file(path='test_data.csv'): #<-- path is test_data.csv ONLY IF it's not specified

    """Generate a CSV file with random numbers and words."""
    with open(path, 'w') as f:
        for i in range(200):
            f.write(str(random.randint(0,100)))
            f.write(',')
            f.write(words[random.randint(0,len(words)-1)])
            f.write('\n')

write_file() #SAME AS write_file('test_data.csv')

with open('test_data.csv', 'r') as f:
    for line in f.readlines():
        number, word = line.split(',')

        l = line.split(',')
        number = l[0]
        word = l[1]

        print('number is '+number+' and word is '+word)
        number = int(number)

        if(number >= 20 and number <= 30):
            print("NUMBER IS BAD! DON'T SAVE THIS!")
