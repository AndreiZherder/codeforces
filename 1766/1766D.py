from math import gcd


def solution():
    n = int(input())
    pairs = []
    for i in range(n):
        pairs.append([int(num) for num in input().split()])
    for a, b in pairs:
        cnt = 0
        while cnt < 101:
            if gcd(a, b) > 1:
                break
            cnt += 1
            a += 1
            b += 1
        print(cnt if cnt < 101 else -1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
