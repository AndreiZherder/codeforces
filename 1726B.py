
def solution():
    n, m = map(int, input().split())
    if m < n:
        print('NO')
        return
    if m % n == 0:
        print('YES')
        print(*(n * [m // n]))
        return
    if n % 2 == 0 and m % 2 == 1:
        print('NO')
        return
    if n % 2 == 1:
        print('YES')
        print(*((n - 1) * [1] + [m - (n - 1)]))
    else:
        print('YES')
        rem = m % n
        num2 = (m + n) // n
        num1 = (m - rem * num2) // (n - rem)
        print(*((n - rem) * [num1] + rem * [num2]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
