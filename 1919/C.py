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
    nums = [int(num) for num in input().split()]
    a = [10 ** 20]
    b = [10 ** 20]
    for num in nums:
        if a[-1] < num and b[-1] < num:
            if a[-1] <= b[-1]:
                a.append(num)
            else:
                b.append(num)
        elif a[-1] >= num and b[-1] >= num:
            if a[-1] - num < b[-1] - num:
                a.append(num)
            else:
                b.append(num)
        elif a[-1] >= num:
            a.append(num)
        else:
            b.append(num)
    ans = 0
    for i in range(1, len(a)):
        if a[i] - a[i - 1] > 0:
            ans += 1
    for i in range(1, len(b)):
        if b[i] - b[i - 1] > 0:
            ans += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
