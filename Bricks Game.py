"""
Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

Input:

First line contains an integer N.

Output:

Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.

"""

"""---SOLUTION---"""

N = int(input())
check = N
for i in range(1, check+1):
    if N>i and N>0:
        N = N-i
    else:
        print('Patlu')
        break
    if N>(i*2) and N>0:
         N = N - 2*i
    else:
        print('Motu')
        break