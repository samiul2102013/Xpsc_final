numbres=[56,9,20,10,45,87,34,70]
odd=[]
for num in numbres:
    if num % 2 == 1 and num % 5 ==0:
        odd.append(num)

print(odd)
odd_num=[num for num in numbres if num % 2==1]
print(odd_num)
name = ['Samiul', 'Momen', 'Feroz']
id =[13,6,37]
a_li=[]
for n in name:
    for i in id:
        a_li.append([n,i])
    
print(a_li)
some = [[n,i] for n in name for i in id]
print(some)