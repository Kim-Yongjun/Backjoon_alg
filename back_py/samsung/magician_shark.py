from operator import is_
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

# 좌 좌상 상 우상 우 우하 하 좌하
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]


def copy_w():
    global arr, cloud
    for i in cloud:
        for j in [1, 3, 5, 7]:
            nx = i[0] + dx[j]
            ny = i[1] + dy[j]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0:
                arr[i[0]][i[1]] += 1


def mov(idx, cnt):
    global arr, cloud
    cou = 0
    for i in cloud:
        nx = i[0] + (dx[idx]) * cnt
        ny = i[1] + (dy[idx]) * cnt
        cloud[cou] = [nx % n, ny % n]
        cou += 1
        arr[nx % n][ny % n] += 1
        is_cloud[nx % n][ny % n] = True


def make_cloud():
    global arr, cloud
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not is_cloud[i][j]:
                tmp.append([i, j])
                arr[i][j] -= 2
    cloud = tmp


for i in move:
    is_cloud = [[False]*n for _ in range(n)]
    mov(i[0]-1, i[1])
    copy_w()
    make_cloud()

answer = 0
for i in range(n):
    for j in range(n):
        answer += arr[i][j]
print(answer)
