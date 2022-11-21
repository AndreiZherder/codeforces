from typing import List


def solution():
    def count(a: List[int]) -> int:
        zero_cnt = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            if a[i] == 0:
                zero_cnt += 1
            else:
                ans += zero_cnt
        return ans

    n = int(input())
    a = [int(num) for num in input().split()]
    if n == 1:
        print(0)
        return
    zero_cnt = 0
    left_zero_index = -1
    right_one_index = -1
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            zero_cnt += 1
            left_zero_index = i
        else:
            if right_one_index == -1:
                right_one_index = i
            ans += zero_cnt

    if left_zero_index != -1:
        a[left_zero_index] = 1
        ans = max(ans, count(a))

    if right_one_index != -1:
        a[left_zero_index] = 0
        a[right_one_index] = 0
        ans = max(ans, count(a))

    print(ans)







def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
