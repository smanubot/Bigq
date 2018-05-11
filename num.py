# Python program to demonstrate 
# basic array characteristics
import numpy as np
# Python code to demonstate String encoding
a = 'jenkinsforclorox'
c = b'GeeksforGeeks'
# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d = a.encode('ASCII')
# checking if a is converted to bytes or not
if (d==c):
    print ("Encoding successful")
else : print ("Encoding Unsuccessful")
