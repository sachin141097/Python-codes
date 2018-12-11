import os
f1 = open("demo.c","r")
if os.path.exists("output.c"):
	os.remove("output.c")
f2 = open("output.c","w")
condition = True

for line in f1.readlines():
	if "//" in line:
		condition = False 
	if condition:
		f2.write(line)
	condition=True
print("Done")
