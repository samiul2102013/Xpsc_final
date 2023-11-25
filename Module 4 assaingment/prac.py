def solve():
    ans = ""
    l=0
    r=0
    subs=[]
    idx=0
    s=input().strip()
    for char in s:
        if char == 'L':
            l+=1
            ans+='L'
        else:
            r+=1
            ans+='R'
        if l==r:
            subs.append(ans)
            ans=""
            idx+=1
    print(idx)
    for i in range(idx):
        print(subs[i])
solve()