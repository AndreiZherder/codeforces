import string
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
    n, t = [int(num) for num in input().split()]
    s1 = input()
    s2 = input()
    same = []
    diff = []
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 == c2:
            same.append(i)
        else:
            diff.append(i)
    ans = list(s1)
    if t >= len(diff):
        for i in diff:
            for c in string.ascii_lowercase:
                if c != s1[i] and c != s2[i]:
                    ans[i] = c
                    break
        t -= len(diff)
        for i in same[:t]:
            for c in string.ascii_lowercase:
                if c != s1[i]:
                    ans[i] = c
                    break
    elif t < ceil(len(diff), 2):
        print(-1)
        return
    else:
        y = len(diff) - t
        x = t - y
        for i in diff[:x]:
            for c in string.ascii_lowercase:
                if c != s1[i] and c != s2[i]:
                    ans[i] = c
                    break
        for i, j in zip(diff[x::2], diff[x + 1::2]):
            ans[i] = s1[i]
            ans[j] = s2[j]
    print(''.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
