#def Welcome():
#    print("Welcome to Python ")
#    print("Good Luck and Enjoy")

#print(Welcome())

#function with arguments
#def Welcome(user):
#    print("Welcome to Python ",user)
#    #print(f"Welcome to Python {user}")   
#    print("Good Luck and Enjoy")

#print(Welcome("Buddy"))

#function add numbers with return value

def addNumbers(no1,no2):
   sum=no1+no2
   return sum

def subtractsNumbers(no1,no2):
   diff=no1-no2
   return diff

def multiplyNumbers(no1,no2):
   prod=no1*no2
   return prod

def divNumbers(no1,no2):
    quo=no1/no2
    return quo

def BasicMath(opr,no1,no2):
   if (opr=="Addition"):
      res=no1+no2
   elif (opr=="Subtraction"):
      res=no1-no2
   elif (opr=="Multiplication"):
      res=no1*no2
   else:
      res=no1/no2
   return res
      
      
def AreaOfRectangle(base,hgt):
    rec=(base*hgt)*1.5
    return rec

area=AreaOfRectangle(4,2)
print("The Area of Rectangle is ",area)

sum=BasicMath("Addition",4,2)
diff=BasicMath("Subtraction",4,2)
prod=BasicMath("Multiplication",4,2)
quo=BasicMath("Division",4,2)

print("The sum of Two Numbers ",sum)
print("The difference of Two Numbers ",diff)
print("The product of Two Numbers ",prod)
print("The quot of Two Numbers ",quo)
