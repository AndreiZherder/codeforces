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
    n = len(s)
    k = int(input())
    c1 = s.count('?')
    c2 = s.count('*')
    c3 = len(s) - c1 - c2
    if k < c3 - c1 - c2:
        print('Impossible')
    elif k < c3:
        m = c3 - k
        ans = []
        cnt = 0
        state = 1
        for letter in s:
            if state == 1:
                if letter in '?*':
                    if ans:
                        ans.pop()
                        cnt += 1
                        if cnt == m:
                            state = 2
                else:
                    ans.append(letter)
            else:
                if letter not in '?*':
                    ans.append(letter)
        print(''.join(ans))
    else:
        m = k - c3
        if m == 0 or c2 > 0:
            ans = []
            state = 1
            for letter in s:
                if letter not in '?*':
                    ans.append(letter)
                elif letter == '*':
                    if state == 1:
                        ans.extend([ans[-1]] * m)
                        state = 2
            print(''.join(ans))
        else:
            print('Impossible')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
