num = input().split()
if len(num) > 5:
    print("Too much input!")
else: 
    max_num = int(num[0])
    for i in num:
        item = int(i)
        if item > max_num:
            max_num = item

print(max_num)