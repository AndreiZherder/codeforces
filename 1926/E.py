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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, k = [int(num) for num in input().split()]
    total = 0
    if k <= ceil(n, 2):
        print(1 + 2 * (k - 1))
    else:
        total += ceil(n, 2)
        cur = 1
        total += (n - pow(2, cur)) // pow(2, cur + 1) + 1
        while k > total:
            cur += 1
            total += (n - pow(2, cur)) // pow(2, cur + 1) + 1
        k -= total - ((n - pow(2, cur)) // pow(2, cur + 1) + 1)
        print(pow(2, cur) + pow(2, cur + 1) * (k - 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
