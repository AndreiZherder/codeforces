from heapq import heappop, heappush
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
    x, k = [int(num) for num in input().split()]
    a = []
    h = []
    m = 0
    for i in range(k):
        l, *nums = [int(num) for num in input().split()]
        a.append(nums[::-1])
        m += l
    for i in range(k):
        heappush(h, (-a[i].pop(), i))
    acc = x
    best = acc
    for j in range(m):
        num, i = heappop(h)
        num = -num
        acc += num
        if acc >= 0:
            best = max(best, acc)
        else:
            break
        if a[i]:
            heappush(h, (-a[i].pop(), i))
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
