
# In the main file which calls all three sprint blocks, create the file
ef= open("Errors.txt","w+")
ef.write("\r\n")
ef.close()

# In each function within the sprint block
ef=open("Errors.txt", "a+")
# Insert the statement that prints the error or pretty table into the f.write statement
ef.write("\r\n")
ef.close()

ef=open("Errors.txt", "r")
if ef.mode == 'r':
    contents = ef.read()
print(contents)


