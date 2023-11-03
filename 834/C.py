from collections import Counter
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
    a, b = [int(num) for num in input().split()]
    x = round((a * b) ** (1 / 3))
    if x ** 3 == a * b and a % x == 0 and b % x == 0:
        print('YES')
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
