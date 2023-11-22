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
    l0, r0 = [int(num) for num in input().split()]
    prev_l = l0
    prev_r = r0
    total = 0
    for i in range(1, n):
        l, r = [int(num) for num in input().split()]
        total += 1 - (prev_r - prev_l + 1 - (prev_r // p - (prev_l - 1) // p)) * (r - l + 1 - (r // p - (l - 1) // p)) / (prev_r - prev_l + 1) / (r - l + 1)
        prev_l = l
        prev_r = r
    total += 1 - (prev_r - prev_l + 1 - (prev_r // p - (prev_l - 1) // p)) * (r0 - l0 + 1 - (r0 // p - (l0 - 1) // p)) / (prev_r - prev_l + 1) / (r0 - l0 + 1)
    print(total * 2000)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
