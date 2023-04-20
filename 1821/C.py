import sys
from collections import Counter
from functools import lru_cache
from itertools import groupby


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def group(s: str) -> str:
        ans = []
        for k, g in groupby(s):
            ans.append(k)
        return ''.join(ans)

    @lru_cache(None)
    def dfs(s: str, depth: int) -> int:
        s1 = s[::2]
        s2 = s[1::2]
        s1 = group(s1)
        s2 = group(s2)
        print(s, s1, s2, depth)
        if len(s1) == 1 or len(s2) == 1:
            return depth
        else:
            return min(dfs(s1, depth + 1), dfs(s2, depth + 1))

    s = input()
    s = group(s)
    if len(s) == 1:
        print(0)
        return
    print(dfs(s, 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
