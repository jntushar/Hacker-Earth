"""
Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

maze

For example if he is at (2, 0) and the command is L he will go to (1, 0).

Input:

Input contains a single string.

Output:

Print the final point where he came out.

"""


"""---SOLUTION---"""

a,b = 0, 0
str = input()
for i in str:
    if i == 'L':
        a = a - 1
    elif i == 'R':
        a = a + 1
    elif i == 'U':
        b = b + 1
    elif i == 'D':
        b = b - 1
print(a, b)