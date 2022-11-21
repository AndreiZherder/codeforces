def solution():
    def check(k: int) -> bool:
        s = sum(a[:k + 1])
        ans = d // (k + 1) * s + sum(a[:d % (k + 1) + 1])
        return ans >= c



    n, c, d = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]

    a.sort(reverse=True)
    if d * a[0] < c:
        print('Impossible')
        return
    if n <= d and sum(a) >= c:
        print('Infinity')
        return
    if n > d and sum(a[:d]) >= c:
        print('Infinity')
        return
    left = 1
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)











def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
