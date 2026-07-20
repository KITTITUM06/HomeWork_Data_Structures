n = int(input())

for row in range(n):
    row_string = ""
    for col in range(n):
        if col == row or col == (n-1) - row:
            row_string = row_string + "* "
        else:
            row_string = row_string + " "
    print(row_string)

    """
    col == row ใช้ ลากเส้นจากซ้ายบนลงขวาล่าง
    col == (n-1) - row  ใช้ลากเส้นจากขวาบนลงซ้ายล่าง
    
    """