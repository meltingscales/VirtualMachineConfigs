import random
from pprint import pprint

letters = 'abcdefghijklmnopqrstuvwxyz'


def get_data():
    x = random.randrange(0, 100)  # get a number between 0-99

    if (x <= 50):
        return "HAH"
    else:
        return x


def create_dirty_file(path='data.csv', times=200):
    f = open(path, 'w')  # open a file named 'path' and write to it, overwriting ALL contents

    for i in range(0, times):  # loop from zero to 200

        f.write(str(get_data()))  # put some data in there!
        f.write(',')  # csv!

        f.write(letters[random.randint(0, len(letters) - 1)])  # random letter

        f.write('\n')
    f.close()


def read_csv(path='data.csv'):
    l = []  # empty list

    with open(path, 'r') as f:  # open the file
        for line in f:  # loop through each line
            line = line.replace('\n', '').replace('\r', '')  # remove newlines
            l.append(line.split(','))  # add each line as a list separated by commas

    return l


def write_csv(path='data.csv', data=[['you', 'need', 'to'], ['give', 'me', 'args']]):
    with open(path, 'w') as f:  # opens the file, deleting all contents

        for row in data:  # go through each row

            f.write(','.join(row))  # joins all row items by commas
            f.write('\n')


def clean_dirty_file(path='data.csv'):
    pass


def generate_excluded_letters(path='data.csv'):
    pass


if __name__ == '__main__':  # if the file is run via command-line
    print("hello")

    create_dirty_file('dirty.csv')  # creates dirty file

    data = read_csv('dirty.csv')  # reads in file we just made
    better_data = []  # meant to hold our filtered data

    print("bad data:")
    pprint(data)

    for line in data:
        if 'H' not in line[0].upper():
            better_data.append(line)

    print("Better data:")
    pprint(better_data)

    write_csv('clean.csv', better_data)  # write csv
