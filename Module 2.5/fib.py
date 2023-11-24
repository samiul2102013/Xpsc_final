def solve(n):
    a=1
    b=2
    c=4
    print('0',' 1',' 1',' 2',end=' ')
    while(c!=n):
        c+=1
        sum=a+b
        print(sum,end=' ')
        a=b
        b=sum
n =int(input())
solve(n)