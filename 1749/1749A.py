def solution():
    n, m = (int(num) for num in input().split())
    for i in range(m):
        input()
    if m < n:
        print('YES')
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
