from collections import defaultdict, deque
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    a, b, c = [int(num) for num in input().split()]
    n = a + b + c
    if a == 0:
        if c != 1:
            print(-1)
        else:
            print(n - 1)
        return
    tree = defaultdict(lambda: [-1, -1, -1])
    tree[0] = [1, 2, 0]
    tree[1][2] = 1
    tree[2][2] = 1
    q = deque([1, 2])
    cur = 3
    a -= 1
    ans = 1
    for i in range(a):
        node = q.popleft()
        level = tree[node][2]
        tree[node][0] = cur
        tree[cur][2] = level + 1
        ans = level + 1
        q.append(cur)
        cur += 1
        tree[node][1] = cur
        tree[cur][2] = level + 1
        ans = level + 1
        q.append(cur)
        cur += 1
    for i in range(b):
        node = q.popleft()
        level = tree[node][2]
        tree[node][0] = cur
        tree[cur][2] = level + 1
        ans = level + 1
        q.append(cur)
        cur += 1
    cnt = 0
    for node in tree:
        if tree[node][0] == -1:
            cnt += 1
    if cnt != c:
        print(-1)
        return
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
