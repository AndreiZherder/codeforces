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
    s = input()
    if s.count('1') == 0:
        print(ceil(n, k + 1))
    else:
        ans = 0
        l = s.find('1')
        ans += l // (k + 1)
        r = s[::-1].find('1')
        ans += r // (k + 1)
        cur = 0
        for i in range(l, n):
            if s[i] == '0':
                cur += 1
            else:
                if cur >= 2 * k + 1:
                    ans += (cur - k) // (k + 1)
                cur = 0
        print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
