person={'name':'Samiul','age':23,'District':'Mymensing'}
print(person)
person['batch'] =13
print(person)
person['name']='Momen'
print(person)
print(person.keys())
print(person.values())
for key, value in person.items():
    print(key,value)