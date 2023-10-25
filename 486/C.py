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
    n, p = [int(num) for num in input().split()]
    s = input()
    half = n // 2
    if p <= half:
        left = 0
        right = half
    else:
        right = n
        if n % 2 == 0:
            left = half
        else:
            left = half + 1
    p -= 1
    s1 = s[::-1]
    to_left = 0
    to_right = 0
    for i in range(left, right):
        if s[i] != s1[i]:
            to_left = max(to_left, p - i)
            to_right = max(to_right, i - p)
    ans = 0
    if to_left == 0:
        ans = to_right
    elif to_right == 0:
        ans = to_left
    else:
        ans = min(to_left, to_right) + to_left + to_right
    for i in range(half):
        ans += min((ord(s[i]) - ord(s1[i])) % 26, (ord(s1[i]) - ord(s[i])) % 26)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
