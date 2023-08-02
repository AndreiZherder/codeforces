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
    n, k = [int(num) for num in input().split()]
    ans = 0
    for i in range(n, n // 2 - 1, -1):
        f2, f1 = n, i
        for j in range(k - 1):
            f2, f1 = f1, f2 - f1
            if f1 < 0:
                break
        else:
            ans += 1
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
