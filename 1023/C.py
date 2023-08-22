from collections import deque
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
    s = list(input())
    ans = []
    cnt = 0
    if n == k:
        print(''.join(s))
        return
    for i in range(n):
        if s[i] == '(':
            ans.append('(')
        else:
            ans.pop()
            cnt += 2
            if cnt == n - k:
                ans.extend(s[i + 1:])
                break
    print(''.join(ans))



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
