file1 = open('codingal.txt','r')
file2 = open('codlingupdated.txt','w')
for line in file1.readlines():
	
	# reading all lines that do not
	# begin with "Coding"
	if not (line.startswith('Coding')):
		
		# printing those lines
		print(line)
		
		# storing only those lines that
		# do not begin with "Coding"
		file2.write(line)


file2.close()
file1.close()
