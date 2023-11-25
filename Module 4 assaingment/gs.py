def solve():
    n = int(input())
    input_line = input()
    elements = input_line.split()
    
    max_number = int(1e7)
    cnt = [0] * (max_number + 1)
    c = 0

    for char in elements:
        k = int(char)
        cnt[k] += 1
        if k == cnt[k]:
            c += k

    print(n - c)

solve()
