def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if sum(a) % 2 == 0:
        print(0)
        return
    good = False
    ans = 0
    while not good:
        ans += 1
        for i in range(n):
            prev = a[i]
            a[i] //= 2
            if (prev % 2) ^ (a[i] % 2):
                good = True
                break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
