def solution():
    n = int(input())
    if n == 0:
        print(n)
        return
    if n % 2 == 0:
        print(n + 1)
    else:
        print((n + 1) // 2)




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
