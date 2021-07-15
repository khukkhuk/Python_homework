def findmax(num):
    length=len(num)
    check = 0
    for x in num:
        if(x>check):
            check = x
        
        if(check==0):
            check = x
            
    return check        

def findmin(num):
    length=len(num)
    check = 0
    for x in num:
        if(x<check):
            check = x
        
        if(check==0):
            check = x
            
    return check  

number = [32,4254,5,2,71,8,456]
print(findmax(number))
print(findmin(number))
