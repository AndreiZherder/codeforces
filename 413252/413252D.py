def solution():
    n = int(input())
    snacks = [int(num) for num in input().split()]
    fallen = [False for i in range(n + 1)]
    j = n
    for snack in snacks:
        if snack == j:
            print(snack, end=' ')
            j -= 1
            while fallen[j]:
                print(j, end=' ')
                j -= 1
            print()
        else:
            fallen[snack] = True
            print()


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
