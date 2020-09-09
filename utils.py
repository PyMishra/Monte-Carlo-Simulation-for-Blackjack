import os, sys

'''Module to suppress and restore printing
as needed'''

# Disable print
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enable_print():
    sys.stdout = sys.__stdout__

'''
print('This will print')
block_print()
print('This won\'t print')
enable_print()
print('This will print too')
'''