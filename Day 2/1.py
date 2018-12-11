count = {}
f = open("demo_file.txt","r")
for word in f.read().split():
	if word in count:
		count[word] += 1
	else:
		count[word] = 1

for word,count in count.items():
	print(word,"",count)

f.close()
