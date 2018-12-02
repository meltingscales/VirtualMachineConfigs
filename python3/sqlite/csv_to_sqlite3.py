import sqlite3

# Connect to sqlite file. This will create a blank '*.db' file if it does not exist.
connection = sqlite3.connect('my_cool_db.db')

# Where's our data file?
data_file_path = 'my_cool_file.csv'

# Execute a CREATE TABLE statement. Note the 'IF NOT EXISTS'.
# This avoids an OperationError if it DOES exist.
connection.execute('''CREATE TABLE IF NOT EXISTS color_table (
    id      INTEGER PRIMARY KEY NOT NULL,
    color   TEXT,
    number  INTEGER,
    fpnum   FLOAT
);
''')

def insert_test_row(connection):
    """Insert a test row of data."""
    cursor = connection.cursor()

    cursor.execute("INSERT INTO color_table(color, number, fpnum) VALUES ('red', 20, 20.1);")

    connection.commit()


# TODO: open my_cool_file.csv and read data

# Open file as read-only
file = open(data_file_path, 'r')

# Consume first line to ignore header.
file.readline()

# For all lines in the file,
for line in iter(file): #NOTE: We use `iter` here to allow us to use __iter__ on the file, i.e. iterate over it.

    # Remove whitespace.
    line = line.strip()

    # Print them!
    print(line)

    # Split the line by a comma and unpack the values into three variables.
    color, number, fpnumber = line.split(',')

    # Convert variables from strings.
    number = int(number)
    fpnumber = float(fpnumber)

    # Print out all separated columns to make sure we did it correctly.
    print(f"Color = {color}")
    print(f"Number = {number}")
    print(f"Color = {fpnumber}")

    # Get a cursor to manipulate the database with.
    cursor = connection.cursor()

    # Construct a 'prepared statement' that inserts `color`, `number`, and
    # `fpnumber` into an INSERT INTO statement.
    cursor.execute("INSERT INTO color_table(color, number, fpnum) VALUES (?, ?, ?);", (color, number, fpnumber))

    # Commit (put changes into database) our query to the database.
    connection.commit()


file.close()
# Close the file.
