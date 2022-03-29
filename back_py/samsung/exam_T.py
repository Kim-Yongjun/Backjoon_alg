n = int(input())
a = list(map(int, input().split()))
l = []
b, c = map(int, input().split())
answer = 0
for i in a:
    answer += 1
    tmp = i - b
    if tmp > 0:
        l.append(tmp)
for i in l:
    if i % c != 0:
        answer += ((i//c)+1)
    else:
        answer += (i//c)
print(answer)
