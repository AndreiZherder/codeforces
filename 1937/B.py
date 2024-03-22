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
    a = []
    a.append(input())
    a.append(input())
    ans = [a[0][0]]
    i = 0
    j = 0
    while j != n - 1:
        if a[i][j + 1] == a[i + 1][j]:
            ans.append(a[i][j + 1])
            j += 1
        elif a[i][j + 1] == '0':
            ans.append(a[i][j + 1])
            j += 1
        else:
            ans.append(a[i + 1][j:])
            ans = ''.join(ans)
            break
    else:
        ans.append(a[1][n - 1])
        ans = ''.join(ans)
    dp = [[0 for j in range(n)] for i in range(2)]
    for j in range(n):
        if ans[j] == a[0][j]:
            dp[0][j] = 1
        else:
            break
    for j in range(n):
        if a[1][j] == ans[j + 1]:
            dp[1][j] = dp[0][j] + dp[1][j - 1]
    print(ans)
    print(dp[1][n - 1])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
