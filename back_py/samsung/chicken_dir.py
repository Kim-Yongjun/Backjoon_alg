from itertools import combinations
n, m = map(int, input().split())
vil = [list(map(int, input().split())) for _ in range(n)]
chic = [[int(i), int(j)] for i in range(n) for j in range(n) if vil[i][j] == 2]
home = [[int(i), int(j)] for i in range(n) for j in range(n) if vil[i][j] == 1]
temp = []
for i in combinations(chic, m):
    temp.append(i)
answer = [0 for _ in range(len(temp))]

for i in range(len(temp)):
    dis = [10e10 for _ in range(len(home))]
    for j in range(len(home)):
        for k in range(len(temp[i])):
            dis[j] = min(dis[j], abs(temp[i][k][0] - home[j]
                                     [0]) + abs(temp[i][k][1] - home[j][1])
                         )
    answer[i] = sum(dis)

print(min(answer))
