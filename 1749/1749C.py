from collections import Counter


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    c = Counter(a)
    k = 1
    while k < 101:
        if c.get(1, 0) < k:
            print(k - 1)
            return
        for i in range(2, k + 1):
            if c.get(i, 0) < 1:
                print(k - 1)
                return
        k += 1
    print(k - 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
