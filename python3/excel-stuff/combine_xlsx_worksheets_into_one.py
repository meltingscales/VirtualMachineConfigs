import os

import pandas as pd

all_data = pd.DataFrame()

filename = 'many_worksheets.xlsx'

sheets = pd.read_excel(filename, sheet_name=None)
# What doing `sheet_name=None` does is get an OrderedDict of each {name:sheet}.


for sheetname, dataframe in sheets.items():
    print(f"{sheetname}:")
    print(dataframe)
    all_data = all_data.append(dataframe, ignore_index=True)

print("Final dataframe:")
print(all_data)

fname, fext = filename.split('.')
fname = fname + '_joined'
output_name = '.'.join((fname, fext,))

print(f"Outputting to {output_name}.")
all_data.to_excel(output_name)
