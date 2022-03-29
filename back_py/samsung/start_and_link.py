from itertools import combinations, permutations
n = int(input())
squad = [list(map(int, input().split())) for _ in range(n)]
pos = []
answer = 1000
for i in combinations(range(n), n//2):
    pos.append(i)
for i in range(len(pos)//2):
    a, b = 0, 0
    for j in permutations(pos[i], 2):
        a += squad[j[0]][j[1]]
    for j in permutations(pos[-i-1], 2):
        b += squad[j[0]][j[1]]
    answer = min(abs(a-b), answer)
print(answer)
