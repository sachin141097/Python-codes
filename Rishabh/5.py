n = int(input("Enter a number : "))
for i in range(2,n//2):
	if n%i == 0:
		print("Not Prime")
		break
else:	
	print("Prime")

