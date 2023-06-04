v = int(input())
a = int(input())
f = int(input())
p = int(input())

vt = a + f + p

if vt <= v:
    print(3)
elif vt > v:
    if a + f <= v:
        print(2)
    elif a + p <= v:
        print(2)
    elif f + p <= v:
        print(2)
        if vt > v and p <= v:
            print(1)
        elif vt > v and f <= v:
            print(1)
        elif vt > v and a <= v:
            print(1)
        else:
            print(0)