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
    stack1 = []
    stack2 = []
    for i, c in enumerate(s):
        if c == 'b':
            if stack1:
                stack1.pop()
        elif c == 'B':
            if stack2:
                stack2.pop()
        elif c.islower():
            stack1.append(i)
        else:
            stack2.append(i)
    indexes = sorted(stack1 + stack2)
    print(''.join(s[i] for i in indexes))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
