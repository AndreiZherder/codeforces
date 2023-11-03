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
    a = sorted(int(num) for num in input().split())
    l = 0
    ans = []
    i = 0
    j = 2 * n - 1
    prevx = a[i]
    prevy = a[j]
    while i < j:
        l += a[i] - prevx + prevy - a[j]
        ans.append((a[i], a[j]))
        prevx = a[i]
        prevy = a[j]
        i += 1
        j -= 1
    print(l)
    for x, y in ans:
        print(x, y)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
