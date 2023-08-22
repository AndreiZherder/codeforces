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


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    n = int(input())
    total = sn(1, n, n)
    s = set(range(1, n + 1))
    ans = []
    cur = total // 2
    k = n
    while cur > 0:
        if cur in s:
            ans.append(cur)
            s.remove(cur)
            cur = 0
        else:
            ans.append(k)
            s.remove(k)
            cur -= k
            k -= 1
    print(total - total // 2 * 2)
    print(len(ans), *ans)







def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
