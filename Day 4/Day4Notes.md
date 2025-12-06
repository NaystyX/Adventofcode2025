# Day 4

Notes for day 4 of the advent of code

## Part 1

We have rolls of paper that we can only access if there are fewer than four rolls of paper in eight adjacent positions. So we will need to read the eight from each roll and then mark if there is a roll or not.

I have 2 functions, first one returns the adjacent objects of the specified position. The second one then checks these if they are @ mark and counts them together, if less than 4 then returns.

## Part 2

Here we have to remove all rolls that are accessible and repeat that until not possible.

I can make another function called remove, that finds accessible rolls and replaces them with ".", and continues this in while true loop until there is no more accessible rolls. In the end it returns the removed amount.