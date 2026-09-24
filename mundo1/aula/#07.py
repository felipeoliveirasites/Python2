print("oi"*5)
print("="*20)
#nome = str(input('Qual é seu nome? '))
#print('Prazer em te conhecer {:=^20}!'.format(nome))
n1= int(input('Digite um número: '))
n2= int(input('Digite outro número: '))
print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1+n2))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('a soma é {},  o produto é {}, a  divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('a divisão inteira é {} e a potência é {}'.format(di, e))