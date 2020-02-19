"""

Alice and Bob are very good friends. They keep on playing some strange games. Today Alice came up with a new game, in which each player gets cards at the start. Each card has it's value printed on it.
The game proceeds as each player chooses a random card and shows it's value. The player having card with higher value wins. As Alice came up with this game, he wants to ensure his win. So he starts to increase value of some cards using an algorithm. To increase the value of a card by , the running time of algorithm is

seconds.
Find the minimum running time of algorithm, ensuring the win of Alice.

Input:
First line of input contains an integer
denoting the number of TestCases.
First line of Each testcase contains two Integers  and .
Next two lines of each TestCase contains  integers, each denoting value of cards of Alice and Bob respectively.

Output:
Print a single line for each TestCase, running time of algorithm to ensure the win for Alice.

"""


"""---SOLUTION---"""

test = int(input())
i = 0
while i < test:
    n, k = [int(x) for x in input().split()]
    alice = list(map(int, input().strip().split()))[:n]
    bob = list(map(int, input().strip().split()))[:n]
    bmax = max(bob)
    j = time = 0
    while j < n:
        if alice[j] <= bmax:
            x = (bmax - alice[j]) + 1
            time += x * k
        j += 1
    print(time)
    i += 1