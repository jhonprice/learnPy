import sys
from math import sqrt

print("The command line args are")


for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')


print("sqrt(25)",sqrt(25))
