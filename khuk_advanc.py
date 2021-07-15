from khuk_basic import *
class advanceMath:

    def __init__(self):
        i=1;
    def min(self,a,b,c):
        if(a>b):
            if(c>a):
                print(b,",",a,",",c)
            
            elif(c>b):
                print(b,",",c,",",a)
                
            else:
                print(c,",",b,",",a)
            
        elif(b>a):
            if(c>b):
                print(a,",",b,",",c)
                
            elif(c>a):
                print(a,",",c,",",b)
            
            else:
                print(c,",",a,",",b)
                
    def max(self,a,b,c):
        if(a<b):
            if(c<a):
                print(b,",",a,",",c)
            elif(c<b):
                print(b,",",c,",",a)
            else:
                print(c,",",b,",",a)
                
        elif(b<a):
            if(c<b):
                print(a,",",c,",",b)
            elif(c<a):
                print(c,",",a,",",b)
            else:
                print(a,",",b,",",c)
            
    def factorial(self,x):
        
        result = 1;

        for i in range(1,x+1):
            result = result * i
            
        return print('result :',result)
    
        
if __name__ == '__main__':
    a = int(input("Enter value 1 : "))
    b = int(input("Enter value 2 : "))
    c = int(input("Enter value 3 : "))
    bm = BasicMath()
    am = advanceMath()
    am.factorial(a)
    am.factorial(b)
    am.factorial(c)
    am.min(a,b,c)
    am.max(a,b,c)
    bm.cal_plus(a,b,c)
    bm.cal_minus(a,b,c)
    bm.cal_mul(a,b,c)
    bm.cal_div(a,b,c)
