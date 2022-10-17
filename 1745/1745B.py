def solution():
    n = int(input())
    ans = [1]
    for i in range(n - 2):
        ans.append(3 + i)
    ans.append(2)
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
