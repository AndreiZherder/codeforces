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
    n, k = [int(num) for num in input().split()]
    if k == 0:
        print(*reversed(range(1, n + 1)))
        return
    ans = []
    for i in range(n, k + 1, -1):
        ans.append(i)
    for i in range(1, k + 2):
        ans.append(i)
    print(*ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
