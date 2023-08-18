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
    s = input()
    carry = 0
    ans = []
    n = len(s)
    last = n
    for i, x in enumerate(reversed(s)):
        x = int(x)
        if x + carry >= 5:
            ans.append(0)
            carry = 1
            last = n - 1 - i
        else:
            ans.append(x + carry)
            carry = 0
    if carry:
        ans.append(1)
        last += 1
    ans.reverse()
    print(''.join(map(str, ans[:last])) + '0' * len(ans[last:]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
