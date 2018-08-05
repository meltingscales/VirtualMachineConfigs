import os
import sys

words = 'cat goose chicken mouse moose squidgeon pidgeon'.split()
ext = 'txt'

for word in words:

	fn = '.'.join([word, ext]) # The filename. cat.txt, goose.txt, etc.
	
	with open(fn, 'w') as f:
		
		print("Writing '{}' to '{}'...".format(word, fn))
		
		f.write(word) # Write 'cat', 'goose', etc.