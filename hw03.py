num = input().split()

if len(num) > 1:
    print("Too much input!")
else:
    n = int(num[0])
    for i in range(1,13):
        print("%d x %d = %d " % (n, i, n * i))