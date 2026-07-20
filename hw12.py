data = input()
data_list = sorted([list(map(int, i.split(","))) for i in data.split(";")])

"""
groups = data.split(";")
temp_list = []
for i in groups:
    items = i.split(",") 
    numbers = [int(items[0]), int(items[1])] 
    temp_list.append(numbers) 
data_list = sorted(temp_list)
"""

output = []
for start, end in data_list:
    for i in range(start, end):
        output.append([i, i+1])

print(str(output).replace(" ", ""))