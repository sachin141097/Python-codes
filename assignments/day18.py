#Print unique values in dictionary
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s = set()
for key in L:
   for val in key.values():
      s.add(val)
print("Unique values:",s)
