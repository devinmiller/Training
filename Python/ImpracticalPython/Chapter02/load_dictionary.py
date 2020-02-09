"""Load a text file as a list

Arguments:
-Text file name (and directory path, if needed)

Exceptions
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires:
-import sys

"""

import sys

def load(file):
    """Open a text file and retirn a list of lowercase strings."""
    try:
        with open(file) as dict_file:
            loaded_txt = dict_file.read().strip().split('\n')
            loaded_txt = map(lambda x: x.lower(), loaded_txt)
            return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening {file}.  Terminating program.', file=sys.stderr)
        sys.exit(1)

