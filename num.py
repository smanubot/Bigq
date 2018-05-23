# Python code to demonstate String encoding
a = 'jenkinsforclorox'
c = b'jenkinsforclorox'
# using encode() to encode the String
# using ASCII mapping
d = a.encode('ASCII')
# checking if a is converted to bytes or not
if (d==c):
    print ("Encoding successful")
else : print ("Encoding Unsuccessful")
