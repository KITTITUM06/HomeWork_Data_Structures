x, y  = map(int, input().split())
for i in range(1, x+1):
    if i % y == 0:
        print(i)
