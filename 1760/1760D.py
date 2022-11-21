def solution():
    n = int(input()) + 2
    a = [2 * 10 ** 5] + [int(num) for num in input().split()] + [2 * 10 ** 5]
    cnt = 0
    valley = False
    for i in range(1, n):
        if a[i] < a[i - 1]:
            valley = True
            continue
        if a[i] == a[i - 1] and valley:
            continue
        if a[i] > a[i - 1] and valley:
            valley = False
            cnt += 1
            if cnt > 1:
                print('NO')
                return
    print('YES')





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
