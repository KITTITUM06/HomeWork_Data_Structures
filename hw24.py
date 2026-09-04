num, fold_size_str = input().split()
fold_size = int(fold_size_str)

chunks = []
for i in range(0, len(num), fold_size):
    chunks.append(num[i:i+fold_size])
total_sum = sum(map(int, chunks))

print(" ".join(chunks))
print(total_sum)