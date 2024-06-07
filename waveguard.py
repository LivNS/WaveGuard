import numpy as np

# dados fictícios para as áreas protegidas pelo Projeto Tamar no Brasil
areas = [
    {'nome': 'Bahia', 'biodiversidade': 9, 'vulnerabilidade': 5, 'conectividade': 8, 'custo': 115},
    {'nome': 'Sergipe', 'biodiversidade': 8, 'vulnerabilidade': 6, 'conectividade': 7, 'custo': 140},
    {'nome': 'Pernambuco', 'biodiversidade': 7, 'vulnerabilidade': 8, 'conectividade': 9, 'custo': 220},
    {'nome': 'Rio Grande do Norte', 'biodiversidade': 6, 'vulnerabilidade': 9, 'conectividade': 6, 'custo': 290},
    {'nome': 'Ceará', 'biodiversidade': 5, 'vulnerabilidade': 6, 'conectividade': 8, 'custo': 170},
    {'nome': 'Espírito Santo', 'biodiversidade': 7, 'vulnerabilidade': 7, 'conectividade': 7, 'custo': 125},
    {'nome': 'Rio de Janeiro', 'biodiversidade': 8, 'vulnerabilidade': 9, 'conectividade': 8, 'custo': 295},
    {'nome': 'São Paulo', 'biodiversidade': 9, 'vulnerabilidade': 9, 'conectividade': 9, 'custo': 210},
    {'nome': 'Santa Catarina', 'biodiversidade': 6, 'vulnerabilidade': 8, 'conectividade': 8, 'custo': 275}
]

# função para calcular o valor de uma área marinha
"""o valor final é uma combinação ponderada desses atributos, ou seja, 
biodiversidade, vulnerabilidade e conectividade, que separamos em "pesos" 
de importancia (respectivamente 50%, 30% e 20%)"""
def calcular_valor_area(area):
    return area['biodiversidade'] * 0.5 + area['vulnerabilidade'] * 0.3 + area['conectividade'] * 0.2 

# função para otimizar a alocação de recursos da area
def otimizar_alocacao(areas, recursos_totais):
    n = len(areas)
    dp = np.zeros((n+1, recursos_totais+1))
    
    for i in range(1, n+1):
        for j in range(1, recursos_totais+1):
            if areas[i-1]['custo'] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-areas[i-1]['custo']] + calcular_valor_area(areas[i-1]))
            else:
                dp[i][j] = dp[i-1][j]
    
# determinar quais áreas marinhas foram selecionados para uma ótima alocação 
    res = []
    w = recursos_totais
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            res.append(areas[i-1]['nome'])
            w -= areas[i-1]['custo']
    
    return dp[n][recursos_totais], res

# Utilizando dados fictícios para encontrar a alocação ótima de recursos
recursos_totais = 300
valor_otimo, areas_selecionadas = otimizar_alocacao(areas, recursos_totais)

print(f'Valor para uma ótima alocação de recursos: {valor_otimo}')
print('Áreas selecionadas para proteção:')
for area in areas_selecionadas:
    print(area)
