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
    a = []
    b = []
    for i in range(n):
        nums = [int(num) for num in input().split()]
        a.append((nums[0], i, 1))
        b.append((nums[1], i, 2))
    ans1 = []
    ans2 = []
    for i in range(n):
        if i < n // 2:
            ans1.append(1)
            ans2.append(1)
        else:
            ans1.append(0)
            ans2.append(0)
    nums = sorted(a + b)
    for num, i, semifinal in nums[:n]:
        if semifinal == 1:
            ans1[i] = 1
        else:
            ans2[i] = 1
    print(*ans1, sep='')
    print(*ans2, sep='')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
