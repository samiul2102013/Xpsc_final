def solve():
    a,b = map(int,input().split())
    if a>b:
        sum=0
        a-=1
        while(a>b):
            if a%2==1:
                sum+=a
            a-=1
        print(sum)
    elif b>a:
        sum=0
        b-=1
        while b>a:
            if b%2==1:
                sum+=b
            b-=1
        print(sum)
t = int(input())
for _ in range(t):
    solve()