# Fibonacci Series using Loop
nNum = 10
num = 0
num1 = 0
num2 = 1
count = 0

while (count<nNum):
    print(num1)
    num = num1 +num2
    num1 = num2
    num2 = num
    count +=1
    
# Recurrence Relation
# Fn = Fn-1 + Fn-2
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nNum = 10
for i in range(nNum):
    print(recur_fibo(i))
