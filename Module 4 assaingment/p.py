def solve():
    n = int(input())
    cnt = {}
    input_line = input()
    elements = input_line.split()
    for element in elements:
        k = int(element)
        if k in cnt:
            cnt[k]+=1
        else:
            cnt[k]=1
    c=0
    for key, value in cnt.items():
        if key<=value:
            c+=key
    print(len(elements)-c)
solve()