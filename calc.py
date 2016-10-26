def isanumber(a):
    boola= True
    try:
        boola=float(a)
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
while (isanumber(no1)==True):

    no1 = input("Enter a number (or a letter to exit): ")
    
    if (isanumber(no1)==True):
        
          
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

            if (isanumber(no2)==False):
                no2 = input("Enter a number: ")

            if isanumber(no2)==True and operator!="/":
                break

            if isanumber(no2)==True and operator=="/" and float(no2)==0:
                print()
                print ( "You can't divide by zero!!! ")
                print()
                no2 = input("Enter a number (different than 0): ")

            if isanumber(no2)==True and operator=="/" and float(no2)!=0:
                break
           
        if operator=="+":
            sume=float(no1)+float(no2)
            

        if operator=="-":
            sume=float(no1)-float(no2)
            

        if operator=="*":
            sume=float(no1)*float(no2)
            
        if operator=="/" and not float(no2)==0:
            sume=float(no1)/float(no2)
        
        print( )
        print ("Result: "+ str(sume))
        print()