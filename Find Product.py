"""
You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo

.

Input Format:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo.

"""


"""---SOLUTION---"""

n = int(input())
numbers = list(map(int, input().strip().split()))[:n]
answer = 1
i = 0
while i < n:
    answer = (answer * numbers[i]) % (1000000000 + 7)
    i += 1
print(answer)