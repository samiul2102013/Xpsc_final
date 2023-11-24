def solve():
    a, b = map(int, input().split())
    a /= 2
    b /= 2
    a = int(a)
    b = int(b)
    if (a-b)==1 or (b-a)==1:
        print(0)
        return

    a = int(a)
    b = int(b)

    if a > b:
        print(a * a - b * b)
    else:
        print(b * b - a * a)

t = int(input())
for _ in range(t):
    solve()
