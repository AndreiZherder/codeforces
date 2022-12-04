def solution():
    n = int(input())
    notebooks = []
    for i in range(n):
        notebooks.append([int(num) for num in input().split()])
    notebooks.sort()
    prev_quality = -10 ** 9
    for price, quality in notebooks:
        if quality < prev_quality:
            print('Happy Alex')
            return
        prev_quality = quality
    print('Poor Alex')


t = 1
while t:
    solution()
    t -= 1