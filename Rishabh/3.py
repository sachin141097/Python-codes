s = input()
num = list(map(int,s.split()))
avg = sum(num)/len(num)
if avg>90:
	print("Grade : Outstanding")
elif avg>80:
	print("Grade : Excellent")
elif avg>50:
	print("Grade : Average")
else:
	print("Fail")
