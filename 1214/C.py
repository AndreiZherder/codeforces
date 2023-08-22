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
    s = input()
    stack = []
    cnt = 0
    for c in s:
        if c == ')':
            if stack:
                stack.pop()
            else:
                cnt += 1
        else:
            stack.append('(')
    if cnt > 1 or len(stack) > 1 or cnt ^ len(stack) == 1:
        print('NO')
    else:
        print('YES')



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
