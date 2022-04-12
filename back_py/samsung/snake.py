import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
#  north, east, south, west
loc = [0, 1, 2, 3]  # 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):  # 사과 있는 곳
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

l = int(input())  # 방향 변환 횟수
dir = deque()
for _ in range(l):  # 우회전은 1 좌회전은 -1
    i, j = input().split()
    if j == 'D':
        dir.append([int(i), 1])
    else:
        dir.append([int(i), -1])

cnt = 0
s = 1  # 첫 방향은 오른쪽
x, y = 0, 0  # 시작 좌표

body = deque()
body.append([0, 0])
bp = False  # 게임 오버 조건
tmp = 0
k = 0
while True:
    if dir:
        i, j = dir.popleft()
    else:
        pass
    while True:
        x += dx[s]
        y += dy[s]
        cnt += 1
        if 0 > x or x >= n or 0 > y or y >= n:
            bp = True
            break

        if board[x][y] == 1:
            if [x, y] in body:
                bp = True
                break
            board[x][y] = 0
            body.append([x, y])
        elif board[x][y] == 0:

            if [x, y] in body:
                bp = True
                break
            body.popleft()
            body.append([x, y])
        if cnt == i:
            break
    if bp:
        break
    s = (s + j+4) % 4
print(cnt)
