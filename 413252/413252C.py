def solution():
    n = int(input())
    if n == 0:
        print(0)
    elif n % 2 == 1:
        print((n + 1) // 2)
    else:
        print(n + 1)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
