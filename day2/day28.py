#swap two numbers
def swap(a,b):
   a,b=b,a
   print("value of a and b after swapping",a,b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("value of a and b before swapping",a,b)
swap(a,b)

