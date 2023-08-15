from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    s = set(range(1, n + 1))
    ans = []
    for i in range(1, n + 1):
        if i in s:
            cur = i
            while cur in s:
                ans.append(cur)
                s.remove(cur)
                cur *= 2
    print(*ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
