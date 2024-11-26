statement = 'gop is a good girl'

# writing in a file 

with open("test.text", "w") as f:
    f.write(s)

fp = open("text.txt",'w') #w = write

fp.write(statement)
fp.close()

#reading a file

with open('text.txt','r') as f:
    s = f.read()
    print(s)

# appending to a file

fp = open("text.txt",'a') #w = write

fp.write(statement)
fp.close()

with open('text.txt','r') as f:
    s = f.read()
    print(s)