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
    def get_score(start: int) -> int:
        best = 0
        cur = 0
        pos = start
        for step in range(m):
            best = max(best, cur + (k - step) * a[pos])
            cur += a[pos]
            pos = p[pos] - 1
        return best


    n, k, pb, ps = [int(num) for num in input().split()]
    pb -= 1
    ps -= 1
    p = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    m = k
    if k >= 2 * n:
        m = n + k % n
    score_b = get_score(pb)
    score_s = get_score(ps)
    if score_b > score_s:
        print('Bodya')
    elif score_b < score_s:
        print('Sasha')
    else:
        print('Draw')





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
