year = int(input())

def is_leap_year(y):
    if( (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) ):
        return True
    return False

if is_leap_year(year):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")