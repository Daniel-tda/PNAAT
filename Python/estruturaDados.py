
# LISTAS

temperaturas_celsius = [25.1, 25.5, 24.9, 26.0, 25.8] #criando uma lista 
print(f"Leituras iniciais de temperatura: {temperaturas_celsius}")

temperaturas_celsius.append(26.2) # adicionando um novo valor 
temperaturas_celsius.append(25.7) 
temperaturas_celsius.append(55.9)
print(f"Leituras após novas coletas: {temperaturas_celsius}")

primeira_leitura = temperaturas_celsius[0] # Acessando o primeiro elemento
terceira_leitura = temperaturas_celsius[2]  # Acessando o terceiro elemento
ultima_leitura = temperaturas_celsius[-1]  # Acessando o último elemento
print(f"Primeira leitura registrada: {primeira_leitura}°C")
print(f"Terceira leitura registrada: {terceira_leitura}°C")
print(f"Última leitura registrada: {ultima_leitura}°C")

temperaturas_celsius[-1] = 25.0  # Modificando a última leitura 
print(f"Leituras após correção: {temperaturas_celsius}")

temperaturas_celsius.pop(0)  # Remove o primeiro elemento 
print(f"Leituras após remover a mais antiga: {temperaturas_celsius}")

# Imprimindo a quantidade de leituras registradas
print(f"Número total de leituras registradas: {len(temperaturas_celsius)}")

# Verificando a presença de um valor específico
if 25.0 in temperaturas_celsius:
    print("A temperatura de 25.0°C está presente nas leituras.")

# Ordenando as leituras em ordem crescente
temperaturas_celsius.sort()
print(f"Leituras ordenadas: {temperaturas_celsius}")

# Ordenando as leituras em ordem decrescente
temperaturas_celsius.sort(reverse=True)  
print(f"Leituras ordenadas (decrescente): {temperaturas_celsius}")


# TUPLAS

constantes = (3.14, 9.81, 299792458) #criando uma tupla
print(f"Constantes físicas: {constantes}")


# DICIONÁRIOS

# Criando um dicionário
estados_maquinas = {
    "maquina_1": "operacional", 
    "maquina_2": "manutencao", 
    "maquina_3": "parada", 
    "maquina_4": "operacional"
}

print(f"Estados iniciais das máquinas: {estados_maquinas}")

# Adicionando novos pares chave-valor ao dicionário
estados_maquinas.update({"maquina_5": "operacional"})
estados_maquinas.update({"maquina_6": "manutencao"})
print(f"Estados após adicionar novas máquinas: {estados_maquinas}")

# Alterando chave-valors existentes
estados_maquinas["maquina_2"] = "operacional"  # Modificando o estado da máquina 2
print(f"Estados após atualização: {estados_maquinas}")

# ou 

estados_maquinas.update({"maquina_3": "manutencao"})  # Modificando o estado da máquina 3
print(f"Estados após atualização: {estados_maquinas}")

# Acessando valores usando chaves
estado_maquina_1 = estados_maquinas["maquina_1"]
estado_maquina_3 = estados_maquinas["maquina_3"]
print(f"O estado da máquina 1 é: {estado_maquina_1}")
print(f"O estado da máquina 3 é: {estado_maquina_3}")
print(f"O estado da máquina 4 é: {estados_maquinas['maquina_4']}")

# Removendo um par chave-valor do dicionário
del estados_maquinas["maquina_3"]  # Remove o estado da máquina 3 (desativada)
print(f"Estados após remover uma máquina: {estados_maquinas}")

# Imprimindo a quantidade de máquinas registradas
print(f"Número total de estados registrados: {len(estados_maquinas)}")

# Listando as chaves do dicionário
print(f"Máquinas atualmente registradas: {estados_maquinas.keys()}")


# TESTES


# Criando um dicionário para armazenar comandos de máquinas
comandos_maquinas = {
    "maquina_A": ["ligar", "monitorar", "desligar"], 
    "maquina_B": ["manutencao", "calibrar"], 
    "maquina_C": ["ligar", "monitorar"], 
    "maquina_D": ["ligar", "desligar"]
}

print(f"\nComandos para as máquinas: {comandos_maquinas}")

# Acessando os comandos de uma máquina específica
proximo_comando = comandos_maquinas["maquina_A"].pop(0)
print(f"Executando comando: {proximo_comando} para a máquina A")
print(f"Comandos restantes para a máquina A: {comandos_maquinas['maquina_A']}")

# Acessando o último comando de uma máquina específica
proximo_comando = comandos_maquinas["maquina_A"].pop(-1) 
print(f"Executando comando: {proximo_comando} para a máquina A")
print(f"Comandos restantes para a máquina A: {comandos_maquinas['maquina_A']}")

# Imprimir um comando específico de uma máquina
print(f"Primeiro comando da máquina C: {comandos_maquinas['maquina_C'][0]}")

# Adicionando nova máquina e seus comandos
nova_maquina = "maquina_E"
comandos_maquinas[nova_maquina] = ["ligar", "monitorar", "desligar"]  
print(f"Comandos após adicionar a máquina E: {comandos_maquinas}")

# Adicionando um novo comando para a máquina B
novo_comando = "ajustar posição"
comandos_maquinas["maquina_B"].append(novo_comando)  
print(f"Comandos para a máquina B após adição: {comandos_maquinas['maquina_B']}")

# Removendo um comando específico da máquina B
comandos_maquinas["maquina_B"].pop(-1)  # Remove o comando "ajustar posição"
print(f"Comandos para a máquina B após remoção: {comandos_maquinas['maquina_B']}")

# Imprimindo quantas máquinas estão registradas
print(f"Máquinas registradas: {len(comandos_maquinas)}")

# Listando as máquinas
print(f"Máquinas atualmente registradas: {comandos_maquinas.keys()}")

# Listando os comandos 
print(f"Comandos das máquinas registradas: {comandos_maquinas.values()}")

# Imprimindo uma máquina e seus comandos
print(f"Máquina defeituosa e seus comandos: {comandos_maquinas['maquina_B']}")

#removendo uma máquina 
comandos_maquinas.pop("maquina_C")
print(f"Comandos após remover a máquina C: {comandos_maquinas}")