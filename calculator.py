def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Choose one of them :")
print ("a.Addition")
print ("b.Substraction")
print ("c.Multiplication")
print ("d.Division")
choice=input ("Enter your choice from a,b,c,d :")
num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))
if (choice=="a"):
    print(num1,"+",num2,"=",add(num1,num2))
elif(choice=="b"):
    print(num1,"-",num2,"=",sub(num1,num2))
elif(choice=="c"):
    print(num1,"*",num2,"=",sub(num1,num2))
elif(choice=="d"):
    print(num1,"/",num2,"=",sub(num1,num2))
