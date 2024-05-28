from os import path
from sys import stdin, stdout
from typing import List

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def solve(a: str, b: str, p1: str, p2: str, indexes: List[int]) -> List[str]:
        forward = [i for i in indexes if s[i] == a]
        backward = [i for i in indexes if s[i] == b]
        if len(forward) == len(backward):
            if len(forward) % 2 == 0:
                j = 0
                while j < len(forward):
                        ans[forward[j]] = p1
                        j += 1
                        ans[forward[j]] = p2
                        j += 1
                j = 0
                while j < len(backward):
                        ans[backward[j]] = p1
                        j += 1
                        ans[backward[j]] = p2
                        j += 1
            else:
                j = 0
                while j < len(forward) - 1:
                        ans[forward[j]] = p1
                        j += 1
                        ans[forward[j]] = p2
                        j += 1
                j = 0
                while j < len(backward) - 1:
                        ans[backward[j]] = p1
                        j += 1
                        ans[backward[j]] = p2
                        j += 1
                ans[forward.pop()] = p1
                ans[backward.pop()] = p1
        else:
            m = min(len(forward), len(backward))
            j = 0
            while j < max(len(forward), len(backward)):
                if j < m:
                    ans[forward[j]] = p1
                    ans[backward[j]] = p1
                    j += 1
                elif j < len(forward):
                    ans[forward[j]] = p1
                    j += 1
                    ans[forward[j]] = p2
                    j += 1
                elif j < len(backward):
                    ans[backward[j]] = p1
                    j += 1
                    ans[backward[j]] = p2
                    j += 1
        return ans


    n = int(input())
    s = input()
    v = [i for i in range(n) if s[i] in 'NS']
    h = [i for i in range(n) if s[i] in 'EW']
    if len(v) % 2 == 1 or len(h) % 2 == 1 or\
            (len(v) == 2 and s[v[0]] != s[v[1]] and len(h) == 0) or\
            (len(h) == 2 and s[h[0]] != s[h[1]]and len(v) == 0):
        print('NO')
        return
    ans = ['' for i in range(n)]
    s1 = solve('N', 'S', 'R', 'H', v)
    s2 = solve('E', 'W', 'H', 'R', h)
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
