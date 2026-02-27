
# Listas

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


# Tuplas

constantes = (3.14, 9.81, 299792458) #criando uma tupla
print(f"Constantes físicas: {constantes}")