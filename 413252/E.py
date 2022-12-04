def solution():
    n = int(input())
    sizes = [int(num) for num in input().split()]
    j = n
    wait = set()
    for size in sizes:
        if size != j:
            print()
            wait.add(size)
        else:
            print(j, end=' ')
            j -= 1
            while j in wait:
                print(j, end=' ')
                j -= 1
            print()


t = 1
while t:
    solution()
    t -= 1