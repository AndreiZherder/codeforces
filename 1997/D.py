from collections import defaultdict
from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def solution():
    def bsr(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            @bootstrap
            def dfs(v: int, w: int) -> int:
                if not g[v]:
                    ans = a[v] >= w
                else:
                    ans = True
                    for u in g[v]:
                        if v == 0:
                            x = 0
                        else:
                            x = w
                        ans = ans and (yield dfs(u, x + w - a[v]))
                yield ans
            return dfs(0, mid)

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


    n = int(input())
    a = [int(num) for num in input().split()]
    p = [-1] + [int(num) - 1 for num in input().split()]
    g = defaultdict(list)
    for i in range(n):
        g[p[i]].append(i)
    print(bsr(0, 3) - 1)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
