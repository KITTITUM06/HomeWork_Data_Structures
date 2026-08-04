n, m = input().split(",")
n = int(n)
m = int(m)

mat = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(i*j)
    mat.append(row)

print(mat)