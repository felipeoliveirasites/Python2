lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudin','Batata frita')

""" for comida in lanche:
    print(f'Eu vou comer {comida}') """

""" for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') """

#print(len(lanche))
#Duplas são imutaveis
#lanche[1] = 'teste'
#print(lanche[1])

""" for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!') """

print(sorted(lanche))
print(lanche)

a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a

print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(4))
print(d.index(5, 1))

pessoa = ('Gustavo', 39,'M',99.88)
del(pessoa[0])
print(pessoa)