# Python Program for Palindrome Number 

num = int(input("Enter a number: ")) 

temp = num 
rev = 0 

while num>0: 
    remain = num % 10 
    rev = (rev * 10) + remain 
    num = num // 10 

if temp == rev: 
    print("Number is palindrome") 
else: 
    print("Number is not palindrome") 
