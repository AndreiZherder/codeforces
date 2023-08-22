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
    s1 = []
    s2 = []
    i = s.find('1', 1)
    if i == -1:
        i = n
    for j in range(i):
        if s[j] == '2':
            s1.append('1')
            s2.append('1')
        else:
            s1.append('0')
            s2.append('0')
    if i < n:
        s1.append('1')
        s2.append('0')
    for j in range(i + 1, n):
        s1.append('0')
        s2.append(s[j])
    print(''.join(s1))
    print(''.join(s2))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
