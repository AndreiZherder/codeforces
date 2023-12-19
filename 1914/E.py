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
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    c = sorted(range(n), key=lambda i: a[i] + b[i], reverse=True)
    ans = 0
    for i in range(0, n - 1, 2):
        ans += a[c[i]] - 1
        ans -= b[c[i + 1]] - 1
    if n % 2 == 1:
        ans += a[c[-1]] - 1
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
