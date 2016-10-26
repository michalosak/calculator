import sys
import os

def isanumber(a):
    boola= True
    try:
        boola=float(a)
        return True
    except:
        boola= False
        return False

def isinteger(a):
    boola= True
    try:
        boola=int(a)
        return True
    except:
        boola= False
        return False

def checkoperator(operator):
    if operator=="+":
        return True
    if operator=="-":
        return True
    if operator=="*":
        return True
    if operator=="/":
        return True
    else:
        return False            


def helpsection():

    if (len(sys.argv)>1):
        if (sys.argv[1]=='--help'):
            print()
            print("================== HELP SECTION =================")
            print()
            print("Welcome User - SIMPLE CALCULATOR help ")
            print()
            print("SIMPLE CALCULATOR can make different operations on integer numbers, so remember to enter integer numbers")
            print("Allowed operators: +, -, *, /")
            print("To exit program enter letter in first number")
            print()
            print("Program should be bulletproof!!! But You can try to crash it! Good luck :)")
            print("Coded by Michał Osak (Codecool Week A)")
            print()
            print("============== END OF HELP SECTION ==============")
            print()
            print()
            return True
    
os.system('cls' if os.name=='nt' else 'clear')
print()
print("============ WELCOME IN SIMPLE CALCULATOR ============")
   
no1=int(0)

while (isinteger(no1)==True):
      
    if helpsection()==True:
        break

    no1='' 
    print()

    while True:
    
        if (isinteger(no1)==False):
           no1 = input("Enter an integer number (or a letter to exit): ")
        if (isanumber(no1)==True and isinteger(no1)==False):
           no1 = input("Enter an integer number (or a letter to exit): ")
        if isinteger(no1)==True:
           break
        if isanumber(no1)==False:
           break
    
    if (isanumber(no1)==False):
        print()
        print("================ HAVE A NICE DAY! BYE! ===============")
        print()
        break
    
    if (isinteger(no1)==True):
        
        while True:
            
            operator=input("Enter an operator: ")
            
            if checkoperator(operator)==True:
                break
            else:
                print()
                print ( "Invalid sign!!! Please focus! Correct signs: +, - , *, / ")
                print()
        
        no2=''

        while True:

            if (isinteger(no2)==False):
                no2 = input("Enter an integer number: ")

            if isinteger(no2)==True and operator!="/":
                break

            if isinteger(no2)==True and operator=="/" and int(no2)==0:
                print()
                print ( "You can't divide by zero!!! ")
                print()
                no2 = input("Enter an integer number (different than 0): ")

            if isinteger(no2)==True and operator=="/" and int(no2)!=0:
                break
           
            sume=int()
        if operator=="+":
            sume=int(no1)+int(no2)
            

        if operator=="-":
            sume=int(no1)-int(no2)
            

        if operator=="*":
            sume=int(no1)*int(no2)
            
        if operator=="/" and not int(no2)==0:
            sume=int(no1)/int(no2)
        
        print("-----------------------------------------------------")
        print ("Result: "+str(no1) + str(operator) + str(no2) +"="+ str(float(sume)))
        print("-----------------------------------------------------")
        
             