"""PROBLEM 7:
What is the 10 001st prime number?"""
#Start making a list of all the prime numbers
prime_nums=[2]
number=3
#Then this loop will check all the numbers until it finds 10001 prime numbers
while (len(prime_nums)<=10000):
    prime=True
    elem=0
    #Here checks if a number is divisible between the previos prime numbers
    while prime==True and elem < len(prime_nums):
        if number%prime_nums[elem]==0:
            #If is divisible, then is not a prime number
            prime=False
        elem+=1
    #If is not divisible, then is a prime number and gets added to the end of the list
    if prime:
        prime_nums.append(number)
    number+=1

print(prime_nums[-1])