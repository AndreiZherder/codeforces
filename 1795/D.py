import sys

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


mod = 998244353


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    ans = ncr(n // 3, n // 6) % mod
    for i in range(0, n, 3):
        w = sorted(a[i:i + 3])
        if w[0] < w[1]:
            continue
        elif w[0] == w[1] and w[1] < w[2]:
            ans = (ans * 2) % mod
        else:
            ans = (ans * 3) % mod
    print(ans)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
