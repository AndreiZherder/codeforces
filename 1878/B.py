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
    ans = [1, 4]
    i = 5
    while len(ans) < n:
        if (3 * i) % (ans[-2] + ans[-1]) == 0 or (ans[-1] + i) % 3 == 0:
            i += 1
        ans.append(i)
        i += 1
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
