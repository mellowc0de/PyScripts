#!python

import re

def rearrange_name(name):
    """ A function that take in a first name and a last name and displays them in reverse order """
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])