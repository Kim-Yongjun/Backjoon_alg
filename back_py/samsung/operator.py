n = int(input())
l = list(map(int, input().split()))
# + - * //
op = list(map(int, input().split()))
maximum = -1e10
minimum = 1e10


def dfs(depth, answer, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(answer, maximum)
        minimum = min(answer, minimum)
        return
    if plus:
        dfs(depth+1, answer + l[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, answer - l[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, answer * l[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(answer / l[depth]), plus, minus, multiply, divide-1)


dfs(1, l[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
