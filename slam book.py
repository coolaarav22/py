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

                        print("\t\t\tSMARTPHONE DIRECTORECTORY", flush=False)
                        print(".............................................")
                        print("\tYOU CAN NOW PERFORM THE FOLLOWING OPERATION ON THIS SLAMBOOK\N")
                        print("1. ADD A NEW CONTACT")
                        print("6.EXIT PHONEBOOK")
                        def add_contact(pb):




                           dip = []
                           for i in range(len(pb[0])):
                              if i == 0:
                                 dip.append(str(input("Enter name:" )))
                                 if i == 1:
                                  dip.append(str(input("Enter name:" )))
                                  if i == 2:
                                      dip.append(str(input("Enter e-mail address:" )))
                                      if i == 3:
                                          dip.append(str(input("Enter date of birth (dd/mm/yy):" )))
                                          if i == 4:
                                              dip.append(str(input("Enter category(family/friend/work/other):" )))
                                          dip.append


                                          return pb 
                                      
                                      def thanks():
                                         

                                         print("................................................")
                                         print("thank you for using our slam book")
                                         print("please visit again")
                                         print(".................................................")
                                         sys.exit("Goodbye,have a nice day ahead")


                                         print(".................................................")
                                         print("hello dear friends,welcome to our slam book")
                                         print("you may now proccreed to explore this slam book and fill your " 
                                         "detaill about your friend")
                                         print("..................................................")



                                         ch = 1
                                         pb = initial_slambook()
                                         while ch in (1,2,3,4,5):
                                          ch = menu()
                                          if ch == 1:
                                       pb = add_contact(pb)
                                 else:
                                   thanks