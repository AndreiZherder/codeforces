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
    a, b, c = [int(num) for num in input().split()]
    r = b % 3
    if r != 0 and 3 - r > c:
        print(-1)
        return
    ans = a + ceil(b, 3)
    if r!= 0:
        c -= 3 - r
    ans += ceil(c, 3)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
