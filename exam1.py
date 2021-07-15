import module1 #เรียกไฟล์

data = module1.data #สร้างออปเจ๊กต์

def cal1(a,b):
    sum1 = a + b
    return sum1

data2 = module1.data2

data3 = module1.data3

print(data['name'])
print(data2['name'])

print(data3['name'][0])
print(data3['name'][1])
print(data3['name'][2])
print(data3['sec'][0])
number = module1.number


print(data3['age'][0])
print(data3['age'][1])
num1 = data3['age'][0]
num2 = data3['age'][1]
sum2 = num1 + num2

print(cal1(num1,num2))

sum1 = cal1(num1,num2)
print(sum1)
