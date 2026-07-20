n = int(input())
for row in range(n):
    row_string = ""    
    for col in range(n):
        row_string = row_string + "* "  
    print(row_string)