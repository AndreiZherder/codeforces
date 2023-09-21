from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    h = [int(num) for num in input().split()]
    start = 0
    while start < n and a[start] > k:
        start += 1
    if start == n:
        print(0)
        return
    best = 1
    cur = 1
    total = a[start]
    i = start + 1
    j = start
    while i < n:
        if h[i - 1] % h[i] != 0 or a[i] > k:
            best = max(best, cur)
            start = i
            while start < n and a[start] > k:
                start += 1
            if start == n:
                print(best)
                return
            cur = 1
            total = a[start]
            i = start + 1
            j = start
        else:
            total += a[i]
            if total <= k:
                cur += 1
                best = max(best, cur)
            else:
                cur += 1
                while j < i and total > k:
                    total -= a[j]
                    j += 1
                    cur -= 1
            i += 1
    best = max(best, cur)
    print(best)






def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
