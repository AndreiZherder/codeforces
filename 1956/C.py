from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [[0 for j in range(n)] for i in range(n)]
    a[0] = list(range(1, n + 1))
    posi = 0
    posj = 0
    ans = []
    ans.append(f'{1} {1} {" ".join(map(str, range(1, n + 1)))}')
    for k in range(n - 1):
        op = 2
        a[posi][posj] = n
        cur = 1
        for i in range(posi + 1, n):
            a[i][posj] = cur
            cur += 1
        cur = n - 1
        for i in range(posi - 1, -1, -1):
            a[i][posj] = cur
            cur -= 1
        posi += 1
        arr = []
        for i in range(n):
            arr.append(a[i][posj])
        ans.append(f'{op} {posj + 1} {" ".join(map(str, arr))}')

        op = 1
        if posi < n:
            a[posi][posj] = n
            cur = 1
            for j in range(posj + 1, n):
                a[posi][j] = cur
                cur += 1
            cur = n - 1
            for j in range(posj - 1, -1, -1):
                a[posi][j] = cur
                cur -= 1
            posj += 1
            arr = []
            for j in range(n):
                arr.append(a[posi][j])
            ans.append(f'{op} {posj + 1} {" ".join(map(str, arr))}')

    total = 0
    for i in range(n):
        for j in range(n):
            total += a[i][j]
    print(total, 2 * n - 1)
    print('\n'.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
