# A number that is divisible only by itself and 1 (i.e. 2, 3, 5, 7, 11) is called Prime Number
# 0 and 1 are not Prime Number

num	=  int(input("Enter  a  number"))

if  num	> 1	:

    for  i  in  range(2, num):
        if	(num % i ==	0 ):
            print(num,"  is  not  a  prime number") 
            break
    else:
        print(num,"is  a  prime  number")

else:
    print(num,"  is  not  a  prime  number")