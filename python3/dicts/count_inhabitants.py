''' The purpose of this script is to count up how many inhabitants each location
has.

Example output:

Hell:       1
Nevada:     3
Illinois:   5
'''

f = open('location_data.txt')

locations = {}


for line in f.readlines():
    line = line.split(',')
    #print('b is: ',b)

    location = line[1] # Remove name, only want location.
    location = location.strip() # Remove newline
    print(location)

    # If location not in dictionary, initialize it to zero.
    if location not in locations:
        locations[location] = 0

    # If location IS in dictionary, we want to add one to it.
    locations[location] += 1

    print(locations)

f = open('location_results.txt', 'w')

for location in locations:

    people = locations[location]

    s = '%-10s: %03d' % ( location, people)
    print(s)

    f.write(s + '\n')

f.close()
