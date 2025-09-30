#simple calculator 

print("welcome to my calculator")

#defined dual!

def add(x , y):
    return x + y 

def subtract(x , y):
    return x - y 

def multiply(x , y):
    return x * y 

def divide(x , y):
    if y == 0:
        print("error : can't divide on zero!")
    else :
        return x / y 
    
#choices for user and make loop with while
while True:
    print(" 1.  add \n 2.  subtract \n 3.  multiply \n 4.  devide \n 5.  exit")

#input choice

    choice = input("choose what you want to do!   ")


#braek loop

    if choice == '5':
       break

#input nums
    if choice in ["1" , "2" , "3" , "4"]:
       num1 = float (input("type num1 : "))
       num2 = float (input("type num2 : "))


#dual progress

    if choice == '1':
       print("result:  ", add(num1 , num2))

    elif choice == '2':
         print("result:  ", subtract(num1 , num2))

    elif choice == '3':
         print("result:  ", multiply(num1 , num2))

    elif choice == '4':
         print("result:  ", divide(num1 , num2))

    else:
        print("please choose number from the list!")

print("\n Thanks for using , have a nice day!")

#end of code 
