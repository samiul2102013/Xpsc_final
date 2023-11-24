def solve(n):
    digits = []  # Create an empty list to store digits
    while n > 0:
        k = n % 10
        digits.append(k)  # Append each digit to the list
        n = n // 10

    # Print the digits in reverse order, separated by space
    print(*digits[:])

T = int(input())
for _ in range(T):
    N = int(input())
    solve(N)
