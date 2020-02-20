"""

You are given a stack of N integers such that the first element represents the top of the stack and the last element represents the bottom of the stack. You need to pop at least one element from the stack. At any one moment, you can convert stack into a queue. The bottom of the stack represents the front of the queue. You cannot convert the queue back into a stack. Your task is to remove exactly K elements such that the sum of the K removed elements is maximised.

Input format :

    The first line consists of two space-separated integers N and K.
    The second line consists of N space-separated integers denoting the elements of the stack.

Output format :

    Print the maximum possible sum of the K removed elements


"""

"""---SOLUTION---"""

if __name__ == "__main__":
    N, K = input().split()
    data = list(map(int, input().strip().split()))[:int(N)]
    result = 0
    K = int(K)
    N = int(N)
    add = [0] * N
    add[0] = data[0]
    for i in range(1, N):
        add[i] = add[i - 1] + data[i]
    for i in range(K):
        temp = add[i] + add[N - 1] - add[N - K + i]
        result = max(result, temp)
    print(result)