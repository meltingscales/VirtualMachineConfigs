import os
import re
id1 = r'^cat[0-9]+?\.txt$'
id2 = r'^dog[0-9]+?\.txt$'

def files_in_dir(path):
    """Given a path, return a list of paths that are inside of it."""
    l = []

    for(dirpath, dirnames, filenames) in os.walk(path):
        l += filenames

    return l

if __name__ == '__main__':

    # Note: __file__ is the current script's directory
    muhfiles = files_in_dir(os.path.dirname(__file__)) #files in the script's directory.

    for filename in muhfiles:
        if re.match(id1, filename) or re.match(id2, filename):
            print("'"+filename+"' matches!")
        else:
            print("'"+filename+"' doesn't match!")
