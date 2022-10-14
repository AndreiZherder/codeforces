import sys


def solution():
    n, m = map(int, input().split())
    # n, m = 1, 1000000
    if m < n:
        print('NO')
        return
    if n == 1:
        sys.stdout.write(f'YES\n{m}\n')
        return
    if m % n == 0:
        sys.stdout.write(f"YES\n{' '.join(map(str, (m // n for i in range(n))))}\n")
        return
    if n % 2 == 0 and m % 2 == 1:
        sys.stdout.write('NO\n')
        return
    if n % 2 == 1:
        sys.stdout.write(f"YES\n{' '.join(map(str, (n - 1) * [1] + [m - (n - 1)]))}\n")
    else:
        rem = m % n
        num2 = (m + n) // n
        num1 = (m - rem * num2) // (n - rem)
        sys.stdout.write(f"YES\n{' '.join(map(str, (n - rem) * [num1] + rem * [num2]))}\n")


def main():
    t = int(input())
    # t = 100000
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
