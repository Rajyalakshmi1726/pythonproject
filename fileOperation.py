file=open('dummy.txt','w')
print(file.write("hello"))
print(file)
print(file.mode)
print(file.name)
print(file.tell())

### operations:
with open('Dummy.txt','w')as file:
    print(file.writeline(), end='')
    print(file.writeline(), end='')
    #print(file.readlines())
    #print(file.tell())
##write mode:
samplefile=open("dummy.txt",'w')
samplefile.write("this is my second line of ")
sample.close()


with open ('Dummy.txt','r') as file:
    for line in file:
        print(line, end='')
