
with open ('Codingal.txt', 'w') as file:
 file.write("hi! I am  penguin I am 1 year old")
 file.close




 with open ('Codingal.txt' , 'r') as file:
  date = file.readlines()
 print('world in this file are . . . .')
for lines in date:
 word = line.split()
 print (word)
 file.close()
