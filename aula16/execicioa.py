# A Tupla (Imutável)
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    # 2. Fazendo o INPUT e convertendo para Inteiro (int)
    # No JS seria: let num = parseInt(prompt("..."))
    num = int(input('Digite um número entre 0 e 20: '))

    # 3. Validação (Python permite essa sintaxe matemática direta)
    if 0 <= num <= 20:
        break # Sai do loop se o número for válido
    
    print('Tente novamente. ', end='')

# 4. Acessando a tupla pelo índice e usando f-string
print(f'Você digitou o número {contagem[num]}')