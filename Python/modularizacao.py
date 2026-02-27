# MÓDULO DE FUNÇÕES
# Podemos criar um arquivo separado para armazenar nossas funções, por exemplo, "funcoes.py", e depois importá-las em outro arquivo, como "main.py".
# No arquivo "funcoes.py", podemos definir nossas funções:

# Importando as funções do módulo

# import

import math
raiz_quadrada = math.sqrt(9) # Exemplo de uso da função sqrt do módulo math
print(f"A raiz quadrada de 9 é: {raiz_quadrada}")

# from import

from datetime import date # Exemplo de uso da função date do módulo datetime

data_hoje = date.today()
print(data_hoje)


#-----------------------------------------------------------------------------------


# Importamos os módulos que serão utilizados no nosso script de monitoramento.
import math
import random
from datetime import datetime

# --- Constantes do Módulo ---
DIAMETRO_ENGRENAGEM_MM = 50
CIRCUNFERENCIA_ENGRENAGEM = math.pi * DIAMETRO_ENGRENAGEM_MM

# --- Funções do Módulo ---
def simular_leitura_sensor():
    """Simula a leitura de sensores de um atuador."""
    posicao_percentual = random.uniform(0, 100)
    temperatura_celsius = random.randint(25, 80)
    return posicao_percentual, temperatura_celsius

# --- Classes do Módulo ---
def registrar_evento(posicao, temperatura):
    """Cria um registro (log) formatado com o status do atuador e um timestamp."""
    timestamp_atual = datetime.now()
    timestamp_formatado = timestamp_atual.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp_formatado}] LOG ATUADOR: Posição={posicao:.2f}%, Temp={temperatura}°C")

# Lógica Principal do Script
print("--- Iniciando Monitoramento Simulado de Atuador Industrial ---")
print(f"Configuração: Circunferência da Engrenagem = {CIRCUNFERENCIA_ENGRENAGEM:.2f} mm")
print("-" * 60)

# Simula o monitoramento por 5 ciclos
for i in range(5):
    pos, temp = simular_leitura_sensor()
    registrar_evento(pos, temp)

print("-" * 60)
print("--- Fim do Monitoramento ---")