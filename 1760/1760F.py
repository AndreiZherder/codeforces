import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def check(k: int) -> bool:
        return d // (k + 1) * sum(a[:k + 1]) + sum(a[:d % (k + 1)]) >= c


    n, c, d = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    a.sort(reverse=True)
    if d * a[0] < c:
        print('Impossible')
        return
    if d > n:
        a.extend([0] * (d - n))
    else:
        while len(a) > d:
            a.pop()
    if sum(a) >= c:
        print('Infinity')
        return
    n = len(a)
    d = n
    left = 0
    right = d - 1
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
