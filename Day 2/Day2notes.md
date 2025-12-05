# Notes

Notes for day 2 puzzle

## Part 1

You are given ranges of IDs and each time they have a sequence of digits repeating they are invalid

I need to first separate the ranges, after that I will make a function which checks the numbers

The function for checking numbers first checks if the number is even, because if not it cant be invalid. After checking the even it will get the midpoint of the number and then check the first half and compare it to the other half, if they are the same it returns True. All True values need to be summed with each other and then that is the answer.

## Part 2

For the part 2 an ID is invalid if the sequence repeats atleast twice. Examples on the page are 12341234 where 1234 is twice and 123123123.

I need to somehow mark or detect all IDs that repeat numbers anyway not only at the middle point. 

We need to check each possible length of blocks of numbers so 2, 3, 4 etc. So we will make a for loop that goes from 1 to midpoint + 1 because any block has to be less or equal to half of the length of the whole number

Then it checks each block for repeating numbers