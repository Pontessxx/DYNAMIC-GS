# Projeto Sentinela: Monitoramento de Poluição Oceânica
![link do projeto](https://github.com/Pontessxx/DYNAMIC-GS)
## Descrição do Projeto

O Projeto Sentinela visa desenvolver uma rede de sensores inteligentes utilizando técnicas de programação dinâmica para otimizar a alocação de sensores subaquáticos e a coleta de dados sobre a poluição oceânica. Este sistema é capaz de identificar áreas críticas de poluição e priorizar ações de monitoramento e resposta, contribuindo para a preservação dos recursos marinhos.

## Funcionalidades Implementadas

### 1. Cálculo da Distância entre Pontos

A função `haversine` calcula a distância entre dois pontos geográficos (latitude e longitude) utilizando a fórmula da distância haversine. Esta função é essencial para determinar a proximidade entre sensores e áreas de interesse.

**Exemplo de Uso:**
```python
lat1 = 34.0522
lon1 = -118.2437
lat2 = 40.7128
lon2 = -74.0060
distancia = haversine(lat1, lon1, lat2, lon2)
print(f"Distância entre os pontos: {distancia} km")
```

### 2. Otimização da Alocação de Recursos
A função `knapsack` utiliza programação dinâmica para resolver o problema da mochila, determinando a alocação ótima de sensores em diferentes locais com base nos valores, pesos e capacidade total. Este algoritmo é fundamental para otimizar a distribuição de recursos limitados.
```python
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value = knapsack(values, weights, capacity)
print(f"Valor máximo de alocação: {max_value}")
```



### 3. Alocação Ótima de Sensores com Dados Fictícios
A função usar_dados_ficticios demonstra a aplicação do algoritmo de otimização utilizando dados fictícios. Esta função considera critérios como biodiversidade, vulnerabilidade e conectividade para calcular a alocação ótima de sensores em uma área marinha.



## Conclusão
O Projeto Sentinela utiliza técnicas avançadas de programação dinâmica para otimizar a alocação de sensores subaquáticos, permitindo uma coleta de dados eficiente e precisa sobre a poluição oceânica. As funções implementadas fornecem uma base robusta para o monitoramento contínuo e a resposta proativa a problemas ambientais, contribuindo para a conservação e a sustentabilidade dos oceanos.



# Programação Dinâmica:

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. MIT Press. Este livro é uma referência abrangente sobre algoritmos, incluindo programação dinâmica.
- Kleinberg, J., & Tardos, E. (2005). Algorithm Design. Pearson. Este livro fornece uma boa introdução à programação dinâmica com muitos exemplos práticos.
- Geodesia e Fórmula de Haversine: de Smith, M. J., Goodchild, M. F., & Longley, P. (2018). Geospatial Analysis: A Comprehensive Guide to Principles, Techniques and Software Tools. Troubador - Publishing. Este livro é uma excelente referência sobre análises geoespaciais.
- Snyder, J. P. (1987). Map Projections: A Working Manual. U.S. Geological Survey Professional Paper 1395. Este manual é uma boa fonte de informações sobre diferentes projeções cartográficas e cálculos geodésicos.