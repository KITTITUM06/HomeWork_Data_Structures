numbers = list(map(int, input().split()))
dict_count = {}

for num in numbers:
    if num in dict_count:
        dict_count[num] += 1
    else:
        dict_count[num] = 1
print(dict_count)