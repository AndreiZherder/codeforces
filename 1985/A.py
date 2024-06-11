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
    word1, word2 = input().split()
    print(word2[0] + word1[1:], word1[0] + word2[1:])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
