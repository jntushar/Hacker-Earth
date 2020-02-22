import sys


def jewelryPieces(adj, cost, walk, value, k):
    pieces = []
    queue = []
    for i in range(k):
        cal = 0
        x = 1
        queue.append(0)
        while queue:
            node = queue.pop(0)
            for p, q in zip(adj[node], cost[node]):
                cal += p * 2
                if cal <= walk[i]:
                    queue.append(p)
                    x += value[p]
                else:
                    break
        queue.clear()
        pieces.append(x)
    return pieces


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m, k = data[0:3]
    data = data[3:]
    walk = data[:4]
    data = data[4:]
    edges = list(zip(zip(data[0:(3 * (n - 1)):3], data[1:(3 * (n - 1)):3]), data[2:(3 * (n - 1)):3]))
    data = data[3 * (n - 1):]
    value = data[:m * 2:2]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    piece = jewelryPieces(adj, cost, walk, value, k)
    for i in piece:
        print(i, end=" ")














