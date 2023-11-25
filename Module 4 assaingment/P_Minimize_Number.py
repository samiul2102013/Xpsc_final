def solve():
    n = int(input())
    input_line = input()
    elements = input_line.split()
    mn=1e9
    for element in elements:
        k = int(element)
        cnt=0
        while k%2==0:
            cnt+=1
            k//=2
        mn = min(mn,cnt)
    print(mn)
solve()