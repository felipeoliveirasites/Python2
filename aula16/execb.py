# Tupla com os times (Dados de exemplo baseados na época do desafio)
times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo',
         'Bahia', 'Cruzeiro', 'Vasco', 'Atlético-MG', 'Internacional',
         'Bragantino', 'Athletico-PR', 'Juventude', 'Criciúma', 'Grêmio',
         'Fluminense', 'Corinthians', 'Vitória', 'Cuiabá', 'Atlético-GO')

print('-=' * 15)
# A) Os 5 primeiros: Slicing igual ao slice() do JS
print(f'Os 5 primeiros são: {times[0:5]}') 

# B) Os últimos 4: O índice negativo no Python é mágico
print(f'Os 4 últimos são: {times[-4:]}')

# C) Ordem Alfabética: sorted() retorna uma NOVA lista ordenada
print(f'Times em ordem alfabética: {sorted(times)}')

# D) Posição da Chapecoense (usando 'Vasco' como exemplo se não houver Chape na lista atual)
time_procurado = 'Vasco'
if time_procurado in times:
    posicao = times.index(time_procurado) + 1
    print(f'O {time_procurado} está na {posicao}ª posição.')
else:
    print(f'O time {time_procurado} não está na série A.')
print('-=' * 15)