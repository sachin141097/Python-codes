#marks and grade
mylist = input("Enter your marks of 5 subjects: ")
mylist = [int(x) for x in mylist.split(',')]
sum = 0    
for number in mylist:    
    sum += number    
avg=sum//len(mylist)
if avg>=90 and avg<=100:
	print("Grade A")
	print("Average:",avg)
elif avg>=80 and avg<=89:
	print("Grade B")
	print("Average:",avg)

elif avg>=70 and avg<=79:
	print("Grade C")
	print("Average:",avg)

elif avg>=60 and avg<=69:
	print("Grade D")
	print("Average:",avg)

elif avg>=50 and avg<=59:
	print("Grade E")
	print("Average:",avg)

elif avg>=40 and avg<=49:
	print("Grade F")
	print("Average:",avg)

elif avg>=30 and avg<=39:
	print("Grade G")
	print("Average:",avg)

