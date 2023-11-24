def solve():
    k = input()
    str_list = []
    for car in k:
        str_list.append(car)
    str_list.reverse()
    print(*str_list)

t = int(input())
while(t):
    t-=1
    solve