n, m = map(int, input().split())
board = [list(input()) for _ in range(m)]
answer = 0
# up down left right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# R B O
pos = [[i, j] for i in range(n) for j in range(m) if board[i][j] == 'R']
pos.extend([i, j] for i in range(n) for j in range(m) if board[i][j] == 'B')
pos.extend([i, j] for i in range(n) for j in range(m) if board[i][j] == 'O')


def move(idx, cnt):
    game = board[:]
    rx, ry, bx, by = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    while True:
        nrx, nry = rx + dx[idx], ry + dy[idx]
        nbx, nby = bx + dx[idx], by + dy[idx]
        if game[nrx][nry] == '.':
