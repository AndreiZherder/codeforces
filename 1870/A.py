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


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    n, k, x = [int(num) for num in input().split()]
    if k > n:
        print(-1)
        return
    if k > x + 1:
        print(-1)
        return
    n1 = k
    n2 = n - n1
    if k == x:
        x-= 1
    print(sn(0, n1 - 1, n1) + n2 * x)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
