start = int(input())
check = start - 1
new = start
cout = 0
while start != check:
    tmp = (new % 10 + new//10) % 10
    new = new % 10*10 + tmp
    check = new
    cout += 1
print(cout)
