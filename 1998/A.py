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


def solution():
    xc, yc, k = [int(num) for num in input().split()]
    ans = []
    if k % 2 == 1:
        ans.append((xc, yc))
        k -= 1
    for i in range(0, k, 2):
        ans.append((xc + i + 2, yc))
        ans.append((xc - i - 2, yc))
    for x, y in ans:
        print(x, y)





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
