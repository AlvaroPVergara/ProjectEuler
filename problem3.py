num=600851475143
pfactors=[]
while (num !=1):
    i=2
    while (num%i!=0 and i!=num):
        i+=1
    num=num/i
    pfactors.append(i)
pfactors.sort()
print(pfactors[-1])

