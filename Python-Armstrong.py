# Armstrong Number in Python
"""
Example : 153 = (1*1*1) + (5*5*5) + (3*3*3) = 153
          1634 = (1*1*1*1) + (6*6*6*6) + (3*3*3*3) + (4*4*4*4) = 1634
"""

num = int(input("Enter a number:"))
sum=0
temp = num

n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print(num,'is Armstrong Number')
else:
    print(num,'is not Armstrong Number')