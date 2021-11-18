"""
Однажды Поликарп опубликовал в социальной сети смешную картинку с опросом про цвет своего хэндла.
Многие из его друзей стали репостить шутку Поликарпа себе в ленту. Некоторые из них репостили репосты и так далее.
Эти события заданы в виде последовательности строк «name1 reposted name2» где name1 — это имя того, кто репостнул,
а name2 — имя того, с чей ленты репостнули шутку.
Гарантируется, что для каждой строки «name1 reposted name2» пользователь «name1» еще не имел эту шутку в свой ленте,
а «name2» уже имел ее в своей ленте к моменту репоста.
Поликарп зарегистрирован под именем «Polycarp», и изначально шутка есть только в его ленте.
Поликарп измеряет успешность шутки как длину наибольшей цепочки репостов. Выведите успешность шутки Поликарпа.
Входные данные
В первой строке входных данных записано целое число n (1≤n≤200) — количество репостов.
Далее записаны сами репосты в порядке их совершения.
Каждый из них записан в отдельной строке и имеет вид «name1 reposted name2».
Все имена во входных данных состоят из прописных или строчных латинских букв и/или цифр
имеют длины от 2 до 24 символов включительно.
Известно, что имена пользователей регистронезависимы, то есть два имени, отличающиеся исключительно регистром букв,
соответствуют одному и тому же пользователю соцсети.
Выходные данные
Выведите единственное целое число — максимальную длину цепочки репостов.
input:
5
tourist reposted Polycarp
Petr reposted Tourist
WJMZBMR reposted Petr
sdya reposted wjmzbmr
vepifanov reposted sdya
output:
6

input:
6
Mike reposted Polycarp
Max reposted Polycarp
EveryOne reposted Polycarp
111 reposted Polycarp
VkCup reposted Polycarp
Codeforces reposted Polycarp
output:
2

input:
1
SoMeStRaNgEgUe reposted PoLyCaRp
output:
2
"""


def dfs(tree: dict, parent: str) -> int:
    if parent not in tree:
        return 0
    return 1 + max((dfs(tree, child) for child in tree[parent]))


def main():
    n = int(input())
    tree = {}
    for _ in range(n):
        child, parent = input().lower().split(' reposted ')
        tree[parent] = tree.get(parent, []) + [child]
    print(1 + dfs(tree, 'polycarp'))


if __name__ == '__main__':
    main()
