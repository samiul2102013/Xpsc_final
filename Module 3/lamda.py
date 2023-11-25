""" def doubled(num):
    return num*2
result=doubled(45) """
doubed=lambda num:num*2
result = doubed(45)
print(result)
squred = lambda num : num*num
result=squred(12)
print(result)

sum = lambda x,y : x+y
result=sum(2,5)
print(result)
numbers=[54,64,6,2,7,8]
doubled_nums = map(doubed,numbers)
""" lamda function also can be used in  """
print(list(doubled_nums))
p = lambda lam : lam*2
result = p(10)
print(p)