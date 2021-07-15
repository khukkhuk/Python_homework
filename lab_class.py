class BasicMath:
    def __init__(self,num1,num2,amount):
        self.num1=num1
        self.num2=num2
        self.amount=amount
        
    def plus(self):
        cal = self.num1 + self.num2
        return cal

    def minus(self):
        num1 = self.num1
        return self.num1-self.num2

    def mul(self):
        return self.num1*self.num2

    
    def div(self):
        return self.num1/self.num2
    
class AdvanceMath(BasicMath):
    def setnum(self,num1,num2,amount):
        self.num1 = num1
        self.num2 = num2
        self.amount = amount
        

    def findMIN(self):
        
        return test
    

num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
amount= []

test=AdvanceMath(num1,num2,amount)
choice = 1
while choice!=0:
    print("1. Plus")
    print("2. Minus")
    print("3. Multiplied")
    print("4. Divide")
    print("------------------------")
    print("5. MIN")
    print("6. MAX")
    print("7. FAC")
    print("0. Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",test.plus())
        
    elif choice==2:
        amount.append(test.minus())
        print("Result: ",test.minus())
    elif choice==3:
        amount.append(test.mul())
        print("Result: ",test.mul())
    elif choice==4:
        amount.append(test.div())
        print("Result: ",test.div())
    elif choice==5:
        print("Result: ",test.findMIN())
    elif choice==0:
        print("Exiting!")
    elif choice==99:
        print("aaaa = ",amount)
    else:
        print("Invalid choice!!")

print()

