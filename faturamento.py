import matplotlib.pyplot as plt

def calcular_percentual_estados(faturamento_estados):
 
  faturamento_total = sum(faturamento_estados.values())
  percentuais = {}
  variacoes = {}

  # Estado de referência (pode ser ajustado)
  estado_referencia = "SP"
  valor_referencia = faturamento_estados[estado_referencia]

  for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    variacao = ((valor - valor_referencia) / valor_referencia) * 100
    percentuais[estado] = percentual
    variacoes[estado] = variacao

  return percentuais, variacoes

# Dados do exemplo
faturamento = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Calcula os percentuais e variações
percentuais, variacoes = calcular_percentual_estados(faturamento)

# Imprime os resultados
for estado, percentual in percentuais.items():
  print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")

# Cria um gráfico de pizza
plt.pie(percentuais.values(), labels=percentuais.keys(), autopct='%1.1f%%')
plt.title("Percentual de Faturamento por Estado")
plt.show()

# Cria um gráfico de barras para a variação percentual
plt.bar(variacoes.keys(), variacoes.values())
plt.xlabel("Estado")
plt.ylabel("Variação Percentual em Relação a SP")
plt.title("Variação Percentual do Faturamento por Estado")
plt.show()