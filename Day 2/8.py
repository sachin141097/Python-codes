def swap(a,b):
	a=a+b
	b=a-b
	a=a-b
	print("After swapping")
	print("Num 1 : ",a)
	print("Num 2 : ",b)
	return

a = int(input("Enter num 1 : "))
b = int(input("Enter num 2 : "))
swap(a,b)

