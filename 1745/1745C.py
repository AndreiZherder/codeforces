def solution():
    n = int(input())
    covers = '0' + input()
    a = [0] + [int(num) for num in input().split()]
    minimum = a[0]
    ones = False
    s = 0
    ans = 0
    for i in range(1, n + 1):
        if not ones:
            if covers[i] == '0':
                minimum = a[i]
                s = a[i]
            else:
                ones = True
                minimum = min(minimum, a[i])
                s += a[i]
        else:
            if covers[i] == '0':
                ones = False
                ans += s - minimum
                minimum = a[i]
                s = a[i]
            else:
                minimum = min(minimum, a[i])
                s += a[i]
    if covers[-1] == '1':
        ans += s - minimum
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
