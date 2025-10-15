# importing the module
import sys



def initial_slambook():
    rows, cols = int(input("please ender number of your")),5



slambook = []
print(slambook)
 
for i in range('rows'):
    print("\nEnder contact %d details in the following order(only):" % (i+i))
    print("NOTE: * indicates mandatory fields")
    print(".....................................................................................................")
    temp = []
    for j in range("cols"):
     temp.append(str(input("Ender name*:")))
if temp[j] ==''or temp [j] =='':
   sys.exit(
            "name is a mandatory field. process exiting due to blank field . . .")
   
   if j == 1:
      temp.append(str(input("ender number*:")))







      if j == 2:
         temp.append(str(input("ender something about your friend")))


         if temp[j] =='' or temp[j] =='': 
            temp[j] = None

            if temp == 3:
               temp.append(str(input("ender date of birth(dd/mm/yy):")))
               if temp[j] =='' or temp[j] =='':
                  

                  temp[j] = None
                  if j == 4:
                     temp.append(str(input("Ender category(family/friend/work/others):")))


                     if temp[j] =='' or temp[j] =='':
                        temp[j] = None

                        slam_book.append(temp)




                        print(slam_book)
                        return slam_book
                     
                     def menu():



                        print("*******************************************************************")