import os
import glob

import pandas as pd

all_data = pd.DataFrame()
output_name = "many_worksheets_joined.xlsx"

try:
	os.remove(output_name)
except OSError:
	pass

for filename in glob.glob("./*.xlsx"): # Go through all xlsx files in this directory

	sheets = pd.read_excel(filename, sheet_name=None)
	# What doing `sheet_name=None` does is get an OrderedDict of each {name:sheet}.


	for sheetname in sheets: # This is a dictionary where a String corresponds to a DataFrame.
		dataframe = sheets[sheetname] # A single DataFrame
		
		print(f"{sheetname}:")
		print(dataframe)
		
		all_data = all_data.append(dataframe, ignore_index=True)

print("Final dataframe:")
print(all_data)


print(f"Outputting to {output_name}.")
all_data.to_excel(output_name)
