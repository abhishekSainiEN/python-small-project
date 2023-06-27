import random

print("press 1 use for make our resume making app")
print("press 2 use for  our calculator  app")
print("press 3 use for rock paper scissor game our  app")


user=int(input("give input:"))

match user:
    case 1:
        while True:

         print("resume maker")

         name=input("give your name:")
         age=int(input("give your age:"))
         gender=(input("give your gender:"))
         number=int(input("give your contact:"))
         email=input("give your email id:")
         qualifiacation=input("give your qualification:")

         print("your resume  was ready")
         print("name:",name)
         print("age:",age)
         print("gender:",gender)
         print("contact:",)
         print("email id:",email+"@gmail.com")
         print("Qualification:" ,qualifiacation)
    case 2:
        while True:

         print("calculator")


         print("press 1 for add \n press 2 or subtract \n press 3 for multiply \n press 4 for devide \n press 5 for "
              "floor dividion \n press 6 for square \n press 7 for exponent \n press 8 for cube")
         select = int(input("select your option"))
         a = int(input("give first number"))


         b = int(input("give second number"))



         if(select==1):
             print("answer..:",a+b)
         elif(select==2):
             print("answer..:",a-b)
         elif (select == 3):
             print("answer..:", a * b)
         elif (select == 4):
             print("answer..:", a / b)
         elif (select == 5):
             print("answer..:", a // b)
         elif (select == 6):
             print("answer..:", a*a)
         elif (select == 7):
             print("answer..:", a**b)
         elif (select == 8):
             print("answer..:", a*a*a)
    case 3:
        print("rock paper scissor game")
        print("Press 1 for rock  \n press 2 for paper \n press 3 for scissor ")
        user=int(input("give your input:::"))
        computer=random.randint(0,3)

        while (True):
            if(user==1 and computer==3 or user ==2 and computer ==1 or user==3 and computer==2):
                print("congratulation you win")
            elif (user == 3 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 3):
                print("better luck next time ' try again ")
            elif(user==computer):
                print("game draw ' try again")
            else:
                print("invalid ")

                print("computer input:",computer)
                print("user input:",user)
            break




