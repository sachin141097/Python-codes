def prime_between(lower,upper):
	li = []
	for i in range(lower,upper+1):
		if i>1:
			for j in range(2,i):
				if i%j == 0:
					break
			else:
				li.append(i)
	return li


lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

li = prime_between(lower,upper)

for i in li:
	print(i,end=" ")
print()

