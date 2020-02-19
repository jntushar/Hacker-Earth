"""

There are three planes , and . Plane will takeoff on every day i.e. , , and so on. Plane will takeoff on every day and plane will takeoff on every day. There is only one runway and the takeoff timing is same for each of the three planes on each day. Your task is to find out the maximum number of flights that will successfully takeoff in the period of

days.

Note: If there is collision between the flights no flight will take off on that day.

Input Format
The first line of the input contains a single integer
, the number of test cases.
Then lines follow each containing four space-separated integers , , and

as denoted in the statement.

Output Format
For each test case print a single integer representing the maximum number of flights that will successfully takeoff in the period of
days.

"""

"""---SOLUTION---"""

test = int(input())
i = 0
while i < test:
    flights = 0
    n, p, q, r = [int(x) for x in input().split(" ")]
    j = 1
    while j <= n:
        if p * j <= n and p * j % q != 0 and p * j % r != 0:
            flights += 1
        if q * j <= n and q * j % p != 0 and q * j % r != 0:
            flights += 1
        if r * j <= n and r * j % p != 0 and r * j % q != 0:
            flights += 1
        j += 1
    print(flights)
    i += 1