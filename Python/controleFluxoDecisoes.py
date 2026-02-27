# ESTRUTURAS CONDICIONAIS

# IF, ELIF, ELSE
'''
temperatura_fabrica = 30

if temperatura_fabrica > 25:
    print("Resfriar a fábrica")

elif temperatura_fabrica < 15:
    print("Aquecer a fábrica")

else:
    print("temperatura estável")


# Simulação de leitura de nível de líquido
nivel_litros = 50  # Nível atual do líquido em litros
nivel_maximo = 100  # Nível máximo permitido em litros
nivel_minimo = 20  # Nível mínimo seguro em litros

print(f'Nível atual do líquido: {nivel_litros} litros')

# Lógica condicional para controle do nível de líquido
if nivel_litros > nivel_maximo:
    print("Atenção: Nível do líquido acima do máximo! Acionando sistema de drenagem.")
elif nivel_litros < nivel_minimo:
    print("Atenção: Nível do líquido abaixo do mínimo! Acionando sistema de abastecimento.")
else:
    print("Nível do líquido dentro dos limites normais.")


# Simulação de leitura de pressão
pressao_atual = 3.5  # Pressão atual em bar
pressao_maxima = 5.0  # Pressão máxima permitida em bar
pressao_minima = 1.0  # Pressão mínima segura em bar

print(f'Pressão atual: {pressao_atual} bar')

# Lógica condicional para controle da pressão
if pressao_atual > pressao_maxima or pressao_atual > 4.5:
    print("Atenção: Pressão crítica! Acionando alívio de pressão.")
elif pressao_atual < pressao_minima or pressao_atual < 2.0:
    print("Atenção: Pressão muito baixa! Acionando compressor.")
else:
    print("Pressão dentro dos limites normais.")

'''
# ESTRUTURAS REPETITIVAS

# WHILE

# Importando a biblioteca necessária para simular o tempo
import time

# Definindo o consumo de energia inicial
consumo_energia = 50  # Consumo inicial em kW
limite_superior = 100  # Limite superior de consumo seguro em kW

# Laço de repetição para monitorar o consumo de energia
while True:  
    print(f"Consumo de energia atual: {consumo_energia} kW")  

    if consumo_energia > limite_superior:
        print("Alerta: Consumo de energia acima do limite seguro!")
        break  # Sai do loop se o limite for ultrapassado

    # Simulando a variação do consumo de energia
    consumo_energia += 10  # Aumenta o consumo em 10 kW
    time.sleep(2)  # Pausa de 2 segundos entre as leituras

print("Monitoramento encerrado.")

'''
# FOR

# O loop irá iterar de 1 a 5, representando cada ciclo de consumo
for ciclo in range(1, 6):
    # Cálculo do consumo de energia para o ciclo atual
    consumo = 50 + (ciclo * 8)
    # Exibe o ciclo e o respectivo consumo de energia em kW
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo} kW")


# O loop irá gerar valores de 1 a 9, pulando de 2 em 2
for ciclo in range(1, 10, 2):  # A cada dois valores
    print(ciclo)  # Exibe o valor atual do ciclo


# FOR COM LISTAS

# Lista com dados simulados de consumo de energia
leituras = [55, 63, 70, 95, 105]  

# Itera sobre cada leitura na lista
for leitura in leituras:
    # Verifica se a leitura de consumo excede o limite de 100 kW
    if leitura > 100:
        print(f"Alerta! Consumo de {leitura} kW excedeu o limite!")
    else:
        print(f"Consumo dentro do limite: {leitura} kW")


# FOR COM DICIONÁRIOS

# Dicionário contendo o consumo de energia em diferentes setores
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

# Itera sobre cada setor e seu respectivo consumo de energia
for setor, consumo in consumo_setores.items():
    # Determina o status do consumo com base no limite de 100 kW
    if consumo > 100:
      status = "acima do limite" 
    else:
      status = "dentro do limite"
    # Exibe o setor, o consumo e o status
    print(f"Setor: {setor} | Consumo: {consumo} kW – Status: {status}")


# Outra forma de iterar sobre o dicionário, acessando apenas as chaves
for setor in consumo_setores:
    if consumo_setores[setor] > 100: # Acessa o valor do consumo usando a chave do setor
        print(f"Alerta! Consumo de {consumo_setores[setor]} kW no setor {setor} excedeu o limite!")
    else:
        print(f"Consumo no setor {setor} dentro do limite: {consumo_setores[setor]} kW")
'''