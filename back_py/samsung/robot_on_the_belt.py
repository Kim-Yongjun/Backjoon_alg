import sys
input = sys.stdin.readline
n, k = map(int, input().split())
belt = list(map(int, input().split()))
on_the_b = list(False for _ in range(n))
cnt = 0


def b_mov():
    global belt, on_the_b, cnt
    tmp = belt[2*n-1]
    belt[1:2*n] = belt[0:2*n-1]
    belt[0] = tmp
    if on_the_b[n-1] == True:
        on_the_b[n-1] = False
    tmp = on_the_b[n-1]
    on_the_b[1:n] = on_the_b[0:n-1]
    on_the_b[0] = tmp
    cnt += 1


def r_on():
    global cnt
    if belt[0] != 0:
        belt[0] -= 1
        on_the_b[0] = True


def r_mov():
    global belt, on_the_b, cnt
    for i in range(n-1, -1, -1):
        if on_the_b[i] and not i+1 < n:
            on_the_b[i] = False
        elif on_the_b[i] and not on_the_b[i+1] and belt[i+1] != 0:
            belt[i+1] -= 1
            on_the_b[i] = False
            on_the_b[i+1] = True


while True:
    b_mov()
    if belt.count(0) >= k:
        break
    r_mov()
    if belt.count(0) >= k:
        break
    r_on()
    if belt.count(0) >= k:
        break
print(cnt)
