"""PROBLEM 6:
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum."""

sum_of_squares=0
square_of_the_sum=0
#first we do a loop and start adding each number to the variable
for num in range(1,101,1):
    #Sum of squares adds de number already squared
    sum_of_squares+=(num**2)
    #Meanwhile, square of the sum adds it normal and after squares everithing
    square_of_the_sum+=(num)
square_of_the_sum=square_of_the_sum*square_of_the_sum
#Then calculate the difference betwen both and print it
difference=square_of_the_sum-sum_of_squares
print(difference)