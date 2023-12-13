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
    s = input()
    l1 = int(s[0] == 'L')
    o1 = int(s[0] == 'O')
    l2 = sum(s[i] == 'L' for i in range(1, n))
    o2 = sum(s[i] == 'O' for i in range(1, n))
    k = 1
    if l1 != l2 and o1 != o2:
        print(k)
        return
    for i in range(1, n - 1):
        k += 1
        l1 += int(s[i] == 'L')
        o1 += int(s[i] == 'O')
        l2 -= int(s[i] == 'L')
        o2 -= int(s[i] == 'O')
        if l1 != l2 and o1 != o2:
            print(k)
            return
    print(-1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
