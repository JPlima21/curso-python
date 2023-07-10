times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atlético-MG', 'Cruzeiro',
        'Flamengo', 'Athletico-PR', 'São Paulo', 'Santos', 'Grêmio',
        'Fortaleza', 'Bragantino', 'Bahia', 'Cuiabá', 'Internacional',
        'Goiás', 'Vasco', 'Corinthians', 'América-MG', 'Coritiba')
print(f'Lista de times: {times}')
print(15 * '-=-')
print(f'os 5 primeiros times são {times[0:5]}')
print(15 * '-=-')
print(f'Os 4 ultimos times são {times[16:]}')
print(15 * '-=-')
print(f'Os times em ordem alfabética {sorted(times)}')
print(15 * '-=-')
print(f'O Corinthians esta na {times.index("Corinthians")+1}º posição')
