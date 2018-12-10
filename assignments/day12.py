n=3
s1=int(input("Enter marks of first subject:"))
s2=int(input("Enter marks of second subject:"))
s3=int(input("Enter marks of third subject:"))
total=s1+s2+s3
avg=total//n
if avg>40:
	print("Congratulation!!!You pass the exam successfully")
else:
	print("Sorry!Better luck next time")

