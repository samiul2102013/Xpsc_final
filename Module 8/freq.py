N, M = map(int, input().split())
array = list(map(int, input().split()))

count_dict = {}

for number in array:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

for i in range(1, M + 1):
    if i in count_dict:
        print(count_dict[i])
    else:
        print(0)
