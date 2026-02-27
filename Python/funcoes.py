# Função para exibir as constantes utilizadas
def constantes():
    pi = 3.14159
    e = 2.71828
    return {
        "pi": pi,
        "e": e
    }

# Chamada
print(f"As constantes utilizadas são: \n{constantes()}")

# Função para exibir a temperatura 
def exibir_temperatura(temp):
    print(f"A temperatura atual é: {temp}°C")

# Chamada
exibir_temperatura(25)

def media_simples(a, b):
    return (a + b) / 2

media = media_simples(80, 100)

# Chamada
print(f"A média é: {media}")
# ou 
print("média:", media_simples(55, 75))

# Função com valor padrão
def verificar_temperatura(valor, limite_maximo=25, limite_minimo=15):
    if valor > limite_maximo:
       return "A temperatura está acima do limite."
    elif valor < limite_minimo:
        return "A temperatura está abaixo do limite."
    else:
        return "A temperatura está dentro do limite."
    
# Chamada
print(verificar_temperatura(28)) # Acima do limite
print(verificar_temperatura(16)) # Dentro do limite
print(verificar_temperatura(10)) # Abaixo do limite
