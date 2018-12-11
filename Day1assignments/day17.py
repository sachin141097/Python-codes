#Remove duplicates from list
namelist=["ramu","shyamu","kanu","manu","ramu","radha","manu"]
final_list = [] 
for name in namelist: 
     if name not in final_list: 
            final_list.append(name) 

for x in final_list:
     print(x) 
