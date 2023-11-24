numbers = [2,5,76,8]
numbers.append(100)
print('appnded numbers are ',numbers)
print(numbers)
my_numbers=[10,20,30]
my_numbers+=numbers
print(my_numbers)
numbers.insert(1,200)
print('numbers after inserting ',numbers)
""" removing first element from the list whose value is x """
if 5 in numbers:
    numbers.remove(5)
print('numbers after removing 5 ',numbers)
numbers.pop(0)
print(numbers)
numbers.pop()
print(numbers)
if 76 in numbers:
    idx = numbers.index(76)
print(idx)
