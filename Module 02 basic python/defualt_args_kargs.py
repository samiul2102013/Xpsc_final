def sum(num1,num2):
    return num1+num2

def parameter(num1,num2,num3=0):
    total = num1+num2+num3
    return total
sum=parameter(5,10)
print(sum)

""" args niye khela """
def all_sum(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
t = all_sum(10,20,30,40,50)
print(t)