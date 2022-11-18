def solution():
    n, s = (int(num) for num in input().split())
    b = {int(num) for num in input().split()}
    maximum = max(b)

    i = 1
    for i in range(1, maximum + 1):
        if i not in b:
            s -= i
    if s < 0:
        print('NO')
        return
    if s == 0:
        print('YES')
        return

    i = maximum + 1
    while s > 0:
        s -= i
        i += 1
    if s < 0:
        print('NO')
        return
    else:
        print('YES')
        return




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
