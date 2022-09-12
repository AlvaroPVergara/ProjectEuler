"""PROBLEM 9:
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a=0
b=0
c=0
finish  =False
#We cacalculate c for each pair of numbers a and b where a and b are < than 1000
while b<1000 and finish==False:
    c=((a**2)+(b**2))**(1/2)
    #Once c is calculated, the program checks if the sum is equal to 1000
    if a+b+c==1000 and a<b<c:
        finish=True
    #If not, then try the next pair of numbers
    else:
        if a<1000:
            a+=1
        if a==1000:
            a=0
            b+=1
print(a,b,c)
print(a*b*c)