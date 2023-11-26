from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
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
    @bootstrap
    def dfs(i: int) -> int:
        if i in cache:
            yield cache[i]
        if g[i][0] == -1 and g[i][1] == -1:
            ans = 0
        else:
            if g[i][0] != -1:
                if s[i] == 'L':
                    ans_left = yield dfs(g[i][0])
                else:
                    ans_left = 1 + (yield dfs(g[i][0]))
            else:
                ans_left = 10 ** 20
            if g[i][1] != -1:
                if s[i] == 'R':
                    ans_right = yield dfs(g[i][1])
                else:
                    ans_right = 1 + (yield dfs(g[i][1]))
            else:
                ans_right = 10 ** 20
            ans = min(ans_left, ans_right)
        cache[i] = ans
        yield ans

    n = int(input())
    s = input()
    g = [[-1, -1] for i in range(n)]
    for i in range(n):
        left, right = [int(num) - 1 for num in input().split()]
        g[i][0] = left
        g[i][1] = right
    cache = dict()
    print(dfs(0))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
