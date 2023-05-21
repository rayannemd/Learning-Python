#q1 nivel 2 fase 1 2020 camisas
#n = int(input())
#t = (str(input()))
#qp = t.count('1')
#qm = t.count('2')
#p = int(input())
#m = int(input())

#q2 nivel senior fase 1 2021 baralho

c = input()
ocorrec = c.count('C')
ocorree = c.count('E')
ocorreu = c.count('U')
ocorrep = c.count('P')

copas = 13 - ocorrec
espadas = 13 - ocorree
ouros = 13 - ocorreu
paus = 13 - ocorrep

print(copas, espadas, ouros, paus)

carta = c % 3

for i in c:
    if carta == carta:
        print("erro")

#if copas and espadas and ouros and paus == 0:
 #   print("0")
    