def combine(a,b):
    dor = f'{a} {b} is the boss'
    return dor
dor=combine('samiul ','hasan')
print(dor)
def famous_name(first,last,*additional):
    total_name=f'{first}, {last}'
    return total_name
total_name=famous_name(last='Hasan',first='Samiul')
print(total_name)