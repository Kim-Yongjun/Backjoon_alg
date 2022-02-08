from pickle import TRUE


while TRUE:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
