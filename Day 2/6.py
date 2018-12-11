def largest(num1,num2,num3):
	l = [num1,num2,num3]
	return max(l)

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))

maximum = largest(num1,num2,num3)
print("Largest number is : ",maximum)

