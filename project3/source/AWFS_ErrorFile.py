

f= open("Errors.txt","w+")

f.write("\r\n")

f.close()

f=open("Errors.txt", "a+")

f=open("Errors.txt", "r")
if f.mode == 'r':
    contents =f.read()
print(contents)


