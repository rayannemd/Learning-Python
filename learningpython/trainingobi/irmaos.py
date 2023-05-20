m = int(input())
a = int(input())
b = int(input())

c = m - a - b
mv = 0

if c > a and c > b:
    mv = c
    if a > c and a > b:
        mv = a
    else: mv = b 
print(mv)