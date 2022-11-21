from collections import defaultdict


def solution():
    n, a, b = (int(num) for num in input().split())
    edges = []
    for i in range(n - 1):
        edges.append((int(num) for num in input().split()))
    tree = defaultdict(list)
    for v, u, w in edges:
        tree[v].append((u, w))
        tree[u].append((v, w))
    print(tree)










def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
