# Function returning None - PCEP Question
def func(a):
    if a == 3:
        return a + 1
    else:
        return

print(func(func(3)) + 2)

# Output
# Traceback (most recent call last):
#   File "c:\Users\...\FUNCTIONS\pcep_question2.py", line 8, in <module>
#     print(func(func(3)) + 2)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'