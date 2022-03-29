import sys
input = sys.stdin.readline
gear = [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())
mov = [list(map(int, input().split())) for _ in range(k)]


def turn(idx, dir):
    global done, gear
    done[idx] = True
    if idx + 1 < 4 and not done[idx+1]:
        if gear[idx][2] != gear[idx+1][6]:
            turn(idx+1, dir * (-1))
    if idx - 1 >= 0 and not done[idx-1]:
        if gear[idx][6] != gear[idx-1][2]:
            turn(idx-1, dir * (-1))
    if dir == 1:
        tmp = gear[idx][7]
        gear[idx][1:8] = gear[idx][0:7]
        gear[idx][0] = tmp
    if dir == -1:
        tmp = gear[idx][0]
        gear[idx][0:7] = gear[idx][1:8]
        gear[idx][7] = tmp


def check_s(l):
    answer = 0
    for i in range(4):
        if l[i][0] == 1:
            answer += (2**i)
    return answer


for i in mov:
    done = list(False for _ in range(4))
    turn(i[0]-1, i[1])
print(check_s(gear))
