file_read = open('codingal.txt','r')
print("file in read mode")
print(file_read.read())
file_read.close()




file_write = open('codingal.txt','w')

file_write.write("file in write mode ..... ")
file_write.write("hi! I am penguin. I am 1 year old")
file_write.close

file_appends = open('codingal.txt','w')

file_appends.appends("file in write mode ..... ")
file_appends.appends("hi! I am penguin. I am 1 year old")
file_appends.close