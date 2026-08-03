text = input()
groups = text.split(";")

parsed_groups = []
for item in groups:
    parts = item.split(",")
    start = int(parts[0])
    end = int(parts[1])
    parsed_groups.append([start,end])
parsed_groups.sort()

result = []
for pair in parsed_groups:
    start = pair[0]
    end = pair[1]

    for i in range(start, end):
        result.append([i, i+1])
print(result)