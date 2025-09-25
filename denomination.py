def no__notes(a):

 Q = [2000,500,200,100,50,20,10,]
 x = 0

for i in range(7): # 0 1 2 3 4 5 6 
 q = notes[i]
 x = a//q
 print("notes of {} = {}".format(q,x))
a = a%q


amout = int(input("ender total amout"))
no__notes(amout)         #4560


