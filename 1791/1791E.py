

def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    mn = 10 ** 20
    cnt = 0
    total = 0
    for num in a:
        if num < 0:
            cnt += 1
        mn = min(mn, abs(num))
        total += abs(num)
    if cnt % 2 == 0:
        print(total)
    else:
        print(total - 2 * mn)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
