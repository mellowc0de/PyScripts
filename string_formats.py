# Basic format string example
name = input('Please enter your first name: ')
number = len(name) * 3
print("Hello {}, your number is {}".format(name, number))

# Alternatively, 
# print("YOur lucky number is {number}, {name}."format(name=name, number=len(name)*3))

# [Operations]
# len(string) -> returns the length of the string 
# for character in string -> iterates over each character in string
# if substring in string -> checks whether substring is in string
# string[i] -> Accesses the character at that index
# string[i:j] -> Accesses the string starting at index i and ending at index j; If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

# [Methods]
# string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
# string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
# string.count(substring) Returns the number of times substring is present in the string
# string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
# string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
# string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
# string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
# delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

# Official Documentation
# https://docs.python.org/3/library/stdtypes.html#string-methods