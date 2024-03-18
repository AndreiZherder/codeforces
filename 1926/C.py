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


def main():
    t = int(input())
    ans = [0 for i in range(2 * 10 ** 5 + 1)]
    mx = 0
    while t:
        n = int(input())
        if ans[n]:
            print(ans[n])
        else:
            for i in range(mx + 1, n + 1):
                ans[i] = ans[i - 1] + sum(int(c) for c in str(i))
            mx = n
            print(ans[n])
        t -= 1


if __name__ == '__main__':
    main()
