
# Leap year
# 2000 is century year

yr = int(input("Enter a year:"))

if yr % 4 == 0:
    if yr % 100 == 0:
        if yr % 400 == 0:
            print("{} is a century leap year" . format(yr))
        else:
            print("{} is not a leap year" . format(yr))
    else:
        print("{} is a simple leap year". format(yr))
else:
    print("{} is not a leap year" . format(yr))
