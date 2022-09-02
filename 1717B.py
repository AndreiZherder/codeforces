from collections import deque


def solution():
    n, k, r, c = map(int, input().split())

    rem = c % k
    s = ['.' for i in range(k)]
    s[rem - 1] = 'X'
    row = deque(n // k * s)
    ans = deque([row])
    row1 = row.copy()
    for i in range(r + 1, n + 1):
        row1.rotate(1)
        ans.append(row1.copy())
    row1 = row.copy()
    for i in range(r - 1, 0, -1):
        row1.rotate(-1)
        ans.appendleft(row1.copy())
    for row in ans:
        print(''.join(row))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
