'''
DS690, Spring2020
Assignment 2 Emily Faber
'''

import random

print("*******************************************************")
for i in range(10): #10 rows
    #prints at the start of every row
    #end = "" does NOT end with a newline
    print("*   ", end = "")
    for i in range(10): #10 columns
        #randrange chooses a number between 0 and the number you give it
        print(random.randrange(10),"   ", end = "")
    print("*") #prints at the end of every row
print("*******************************************************")
