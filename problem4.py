largest_palindrome=[0,0,0]
for i in range(1000):
    for n in range(1000):
        mul=i*n
        mul=str(mul)
        pal=True
        for j in range((len(mul)//2)+1):
            if mul[j-1]!=mul[-j]:
                pal=False
        mul=int(mul)
        if pal==True and mul>largest_palindrome[0]:
            largest_palindrome[0]=mul
            largest_palindrome[1]=i
            largest_palindrome[2]=n
print(largest_palindrome)