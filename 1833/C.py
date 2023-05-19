import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    has_even = False
    has_odd = False
    min_odd = 10 ** 20
    for num in a:
        if num % 2 == 0:
            has_even = True
        else:
            has_odd = True
            min_odd = min(min_odd, num)
    if has_odd and not has_even:
        print('YES')
        return
    if has_even and not has_odd:
        print('YES')
        return
    if all(num - min_odd > 0 for num in a if num % 2 == 0):
        print('YES')
        return
    if all(num - min_odd > 0 for num in a if num % 2 == 1):
        print('YES')
        return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
