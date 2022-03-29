import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
table = [[0]*n for _ in range(n)]
bf = defaultdict(list)
answer = 0

for _ in range(n**2):
    input_ = list(map(int, input().split()))
    bf[input_[0]] = input_[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_emp = -1

    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                like_cnt = 0
                emp_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if table[nx][ny] in input_:
                            like_cnt += 1
                        if table[nx][ny] == 0:
                            emp_cnt += 1
                if max_like < like_cnt or (max_like == like_cnt and max_emp < emp_cnt):
                    max_x = i
                    max_y = j
                    max_like = like_cnt
                    max_emp = emp_cnt
    table[max_x][max_y] = input_[0]
for i in range(n):
    for j in range(n):
        cnt = 0
        like = bf[table[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            answer += 10**(cnt-1)


print(answer)
