myfile = open('unsorted.txt', 'r')

a = []

for line in myfile.readlines(): # Go through all lines in our file, separated by [ENTER] key
    line = line.strip() # Remove extra newlines/whitespaces

    try:
        n = float(line) # Turn a string into a number
        a.append(n) # Add our number onto the end of our list
        print(n)
    except ValueError as e: # If we try to turn 'hi' or 'dog' into a number, don't do it.
        print("'" + line + "' is a crappy value. Not converting.")

a.sort() # Sort list.
print(a)
