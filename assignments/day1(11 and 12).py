def create_rec(Number,Name,Age,Marks):
	rec3 = [Number,Name,Age,Marks]
	rec1.append(rec3)

def append_rec(rec1):
	rec2 = [3, "Radha", 17, "75%"]
	rec1.append(rec2)
rec1 = []
create_rec(1, "ram", 18, "65%")
create_rec(2, "shyam", 17, "70%")
append_rec(rec1)

print(rec1)
