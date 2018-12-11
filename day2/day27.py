#maximum of three numbers
def maximum(n1,n2,n3):
  numlist=[n1,n2,n3]
  return max(numlist)
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
print(maximum(n1,n2,n3))
