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


no1=int(0)

print("============ WELCOME IN SIMPLE CALCULATOR ============")


while (isinteger(no1)==True):
      
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
        
             