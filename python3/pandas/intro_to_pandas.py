from pprint import pprint

import pandas as pd

df = pd.read_excel('cool.xlsx')

print(df)

df['c'] = df['c'].astype('str')  # Allow putting strings in `c` column.
df['ignore'] = df['ignore'].astype('bool')
df['over_number'] = df['over_number'].astype('bool')

df_deleted = df.copy(deep=True)
df_deleted.drop(df.index, inplace=True)

UPPER_THRESHOLD = 99
LOWER_THRESHOLD = 16

print("1.  Combine `A` and `B` into `C` by concatenation.")
for i, row in df.iterrows():
    # print("Row is:")
    # print(row)

    a = str(row['a'])
    b = str(row['b'])

    concat = a + b

    df.set_value(i, 'c', concat)
print(df)

print("2.  Count all the duplicates of `C` and store them in `D`.")
seen = {}
for i, row in df.iterrows():  # Count 'em up
    c = row['c']

    if c not in seen:  # Haven't seen letter before
        seen[c] = 0

    seen[c] += 1  # Seen letter `c` once, add one.

for i, row in df.iterrows():  # Put the recorded numbers in
    c = row['c']

    times_seen = seen[c]

    df.set_value(i, 'd', times_seen)
pprint(seen)
print(df)

print("3. Ignore all rows where `D` is `1`.")
for i, row in df.iterrows():
    d = row['d']

    if d == 1.0:
        df.set_value(i, 'ignore', True)
    else:
        df.set_value(i, 'ignore', False)

print(df)

print("4. Move all rows to a different place where `F` is `CANCELLED` and `D` is NOT `1`.")
delete_these = []
for i, row in df.iterrows():
    f = row['f']
    d = row['d']

    if str(f) == 'CANCELLED' and d != 1.0:
        delete_these.append(i)
        df_deleted = df_deleted.append(row)
        # We need to save the Series, `row`, into `df_deleted`.

df.drop(delete_these, axis=0, inplace=True)

print(df)
print(df_deleted)

print("""5.  If any value in `G` is over `100`, and any other row with 
the same `C`'s `G` is less than `16`, then delete the row with the value less than `16`.""")
over_numbers = {} # Create a dictionary to store which rows are over a number
for i, row in df.iterrows():  # Determine if it's over a number
    c = row['c']
    g = row['g']

    if g > UPPER_THRESHOLD:
        over_numbers[c] = True

print(over_numbers)

for i, row in df.iterrows():  # Store whether or not it's over a number in the DataFrame
    c = row['c']

    if c in over_numbers:
        df.set_value(i, 'over_number', True)
    else:
        df.set_value(i, 'over_number', False)

print(df)

delete_these = []
for i, row in df.iterrows(): # Remove all rows that have over_number=True and 'g'<100
    g = row['g']
    over_number = row['over_number']

    if g <= LOWER_THRESHOLD and over_number is True: # If g <= 16 and over_number=True
        delete_these.append(i) # Write down the row number to drop later
        df_deleted = df_deleted.append(row) # Add the row to our other DataFrame

df.drop(delete_these, axis=0, inplace=True)
print(delete_these)
print(df)
print(df_deleted)

writer = pd.ExcelWriter('cool_output.xlsx')
df.to_excel(excel_writer=writer)
writer.save()

writer = pd.ExcelWriter('cool_output_deleted.xlsx')
df_deleted.to_excel(excel_writer=writer)
writer.save()