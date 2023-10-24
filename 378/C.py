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


d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))


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
    def dfs(i: int, j: int):
        for di, dj in d4:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in seen and a[ni][nj] == '.':
                seen.add((ni, nj))
                yield dfs(ni, nj)
                if remaining[0]:
                    a[ni][nj] = 'X'
                    remaining[0] -= 1
        yield


    n, m, k = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                x, y = i, j
    seen = {(x, y)}
    remaining = [k]
    dfs(x, y)
    for row in a:
        print(''.join(row))



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
