# prime numbers in range
primelist=[]
def primeinrange(lower,upper):
    
    for num in range(lower,upper+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                primelist.append(num)
    return primelist
lower=int(input("Enter lower bound"))
upper=int(input("Enter upper bound"))
primeinrange(lower,upper)
print(primelist)
            
