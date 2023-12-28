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
    vowels = set('ae')
    consonants = set('bcd')
    ans = []
    i = 0
    s = s[::-1]
    while i < n:
        if s[i] in vowels:
            ans.append(s[i:i + 2][::-1])
            i += 2
        else:
            ans.append(s[i:i + 3][::-1])
            i += 3
    print('.'.join(ans[::-1]))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
