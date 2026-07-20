n = int(input())
for i in range(n):
    spaces_rows = (n - 1) - i
    rows = " " * spaces_rows + "/"
    print(rows)