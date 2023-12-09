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
    a, b = [int(num) for num in input().split()]
    xk, yk = [int(num) for num in input().split()]
    xq, yq = [int(num) for num in input().split()]
    if a != b:
        d = ((a, b), (b, a), (-a, -b), (-b, -a), (-a, b), (-b, a), (a, -b), (b, -a))
    else:
        d = ((a, b), (-a, -b), (-a, b), (a, -b))
    ans = 0
    for dx, dy in d:
        x = xk + dx
        y = yk + dy
        for dx1, dy1 in d:
            if xq == x + dx1 and yq == y + dy1:
                ans += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
