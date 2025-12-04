# Notes

Notes for day 1 of advent of code

## Part 1

Numbers from 0 to 99

L, R direction

Number after direction tells how much to turn

The password is the amount of times the dial is at 0, dial starts from 50

I will need to first get the direction of a line in moves.txt, then the number. Each time the dial variable is 0 add 1 to the password.

I made function get_direction so that if direction is R return 1, if L return -1, otherwise 0. 

Function get_steps return number after direction

After that I just have a while loop that loops through every move and if dial is at 0 at any point it makes counter go up

My first version got me the wrong result which is where I realised I had to add a check in the steps so that the dial doesn't go under 0 or over 99, this was done with for loop so that each step is counted on it's own

## Part 2

If I understood correctly I have to change my dial check to inside my for step loop to make it count each time.

And my thoughts were correct, in part 2 I moved my if dial == 0 check inside the for loop and got the correct result. In my code both part 1 and part 2 are marked, part 1 is commented out