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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    xs = [abs(int(num)) for num in input().split()]
    order = sorted(range(n), key=lambda i: xs[i])
    hps = [0 for i in range(n + 1)]
    for i in order:
        hps[xs[i]] += a[i]
    power = k
    for i in range(1, n + 1):
        if power < hps[i]:
            print('NO')
            return
        power += k - hps[i]
    print('YES')



def main():
    t = int(input())
    i = 0
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
