import math

# Função para calcular a distância entre dois pontos (latitude e longitude)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

# Função para encontrar a distribuição ótima dos sensores usando programação dinâmica
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Função para calcular a alocação ótima dos sensores com base em dados fictícios
def usar_dados_ficticios():
    sensors = [
        {"id": 1, "value": 50, "weight": 10, "latitude": 0.1, "longitude": 0.1, "biodiversity": 8, "vulnerability": 7, "connectivity": 6},
        {"id": 2, "value": 60, "weight": 20, "latitude": 0.2, "longitude": 0.2, "biodiversity": 7, "vulnerability": 8, "connectivity": 5},
        {"id": 3, "value": 70, "weight": 30, "latitude": 0.3, "longitude": 0.3, "biodiversity": 6, "vulnerability": 6, "connectivity": 8},
        {"id": 4, "value": 80, "weight": 40, "latitude": 0.4, "longitude": 0.4, "biodiversity": 9, "vulnerability": 5, "connectivity": 7},
    ]
    capacity = 50
    values = [(sensor["value"] + sensor["biodiversity"] * 2 + sensor["vulnerability"] * 1.5 + sensor["connectivity"] * 2) for sensor in sensors]
    weights = [sensor["weight"] for sensor in sensors]

    max_value = knapsack(values, weights, capacity)
    print(f"Valor máximo de alocação (considerando critérios): {max_value}")

    for sensor in sensors:
        print(f"Sensor ID: {sensor['id']}, Localização: ({sensor['latitude']}, {sensor['longitude']})")
        print(f"Biodiversidade: {sensor['biodiversity']}, Vulnerabilidade: {sensor['vulnerability']}, Conectividade: {sensor['connectivity']}")

def main():
    while True:
        print("\nSelecione o algoritmo que você deseja utilizar:")
        print("1. Calcular a distância entre dois pontos")
        print("2. Otimizar a alocação de recursos")
        print("3. Usar dados fictícios para encontrar a alocação ótima de recursos")
        print("4. Sair")
        escolha = int(input("Digite sua escolha (1-4): "))
        
        if escolha == 1:
            lat1 = float(input("Digite a latitude do primeiro ponto: "))
            lon1 = float(input("Digite a longitude do primeiro ponto: "))
            lat2 = float(input("Digite a latitude do segundo ponto: "))
            lon2 = float(input("Digite a longitude do segundo ponto: "))
            distancia = haversine(lat1, lon1, lat2, lon2)
            print(f"Distância entre os pontos: {distancia} km")
        elif escolha == 2:
            values = list(map(int, input("Digite os valores dos itens separados por espaço: ").split()))
            weights = list(map(int, input("Digite os pesos dos itens separados por espaço: ").split()))
            capacity = int(input("Digite a capacidade da mochila: "))
            max_value = knapsack(values, weights, capacity)
            print(f"Valor máximo de alocação: {max_value}")
        elif escolha == 3:
            usar_dados_ficticios()
        elif escolha == 4:
            print("Saindo...")
            break
        else:
            print("Escolha inválida, por favor selecione uma opção válida.")

if __name__ == "__main__":
    main()