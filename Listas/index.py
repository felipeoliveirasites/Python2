""" num = [2,5,9,1]
#num[2]=9
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
#num.pop(2)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Esta lista tem  {len(num)} elementos') """

valore = []
""" valore.append(5)
valore.append(9)
valore.append(4) """

""" for cont in range(0,5):
    valore.append(int(input('Digite um valor: ')))

for c,v in enumerate(valore):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao fina da lista.') """

a = [2,3,4,7]
b = a[:] # copia
b[2]=8

print(f'Lista A: {a}')
print(f'Lista B: {b}')