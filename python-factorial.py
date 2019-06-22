# Factorial Using Loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1,num+1):
   fact = fact * i 

print("Factorial of ",num, "is :",fact)

# Factorial Using Recursive Function
def fact_recur(n):
   if n==0:
      return 1
   else:
      return(n*fact_recur(n-1))

num = 4
print("Factorial of",num,"is",fact_recur(num))
