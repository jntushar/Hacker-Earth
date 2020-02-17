"""
You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers l, r and k.

Output Format
Print the required answer on a single line. 
"""


"""---SOLUTION---"""

l, r, k = [int(x) for x in input().split(" ")]
count = 0

while l <= r:
    if l % k == 0:
        count += 1
    l += 1
print(count)