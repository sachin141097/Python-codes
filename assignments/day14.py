#largest of three numbers
mylist = input("Enter 3 numbers: ")
num1,num2,num3 = [int(x) for x in mylist.split(',')]
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("largest is:",largest)

