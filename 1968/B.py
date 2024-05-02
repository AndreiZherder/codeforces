from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = input()
    b = input()
    j = 0
    for k in range(n):
        while j < m and b[j] != a[k]:
            j += 1
        if j == m:
            print(k)
            return
        else:
            j += 1
    print(n)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
