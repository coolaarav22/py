#read first line of file
file = open('Codingal.txt','r')
print("Reading first line...")
print(file.readline())
file.close()


#read first three lines of file
file = open('Codingal.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()



file = open('codingal.txt','r')
print('looping through the line')

for line in file:
    print(line)
    file.close()