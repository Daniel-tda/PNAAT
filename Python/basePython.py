print("hello world")

numero_str = "10"
numero_int = int(numero_str)
print(numero_int)

numero_int2 = 20
numero_str2 = str(numero_int2)
print(numero_str2)

numero_float = 3.14
numero_str3 = str(numero_float) 
print(numero_str3)

numero_int3 = 0
boolean_val = bool(numero_int3)
print(boolean_val)

numero_int4 = 1
boolean_val2 = bool(numero_int4)
print(boolean_val2)

a,b,c = 1,2,3
d=e=f = 3
print(a,b,c)
print(d,e,f)

# operadores diferentes
A,B,C = 1, 5, 8

print(C % B) # resto da divisão de C por B
print(C ** A) # C elevado a A
print(C // B) # divisão inteira de C por B (sem considerar o resto)

print(A + B * C) # multiplicação tem precedência sobre adição
print((A + B) * C) # parênteses alteram a ordem de avaliação

print(A != B) # A é diferente de B (sará True)

# operadores lógicos

print(A < B and C > A) # A é menor que B e C é maior que A (será True)
print(A != B and C > A) # A é diferente de B e C é maior que A (será True)
print(A > B or C > A) # A é maior que B ou C é maior que A (será True)
print(A == B or A > C) # A é igual a B ou A é maior que C (será False)
print(not (A < B)) # negação de A é menor que B (será False)

# Expressões Condicionais Complexas
# Combinando operadores lógicos e de comparação

# Definindo variáveis
x = 8
y = 12
z = 20

# Expressão complexa com operadores condicionais
expressao_condicional = (x > y and y < z) or (x + y > z and not (z == x * 2))
print(f"Expressão Condicional: {expressao_condicional}") 

# Outra expressão complexa
outra_expressao_condicional = (x < y and y == z) or (x + z > y and not (x == z / 2))
print(f"Outra Expressão Condicional: {outra_expressao_condicional}") 

# Expressões Relacionais Complexas
# Combinando operadores matemáticos, lógicos e de comparação

# Definindo variáveis
m = 15
n = 25
p = 35

# Expressão complexa combinando diferentes operadores
expressao_relacional = ((m * n) > (p + m)) and ((p / n) < m) or not (p == m + n)
print(f"Expressão Relacional: {expressao_relacional}") 

# Outra expressão relacional complexa
outra_expressao_relacional = ((m + n - p) * (p / m) > n) and ((m ** 2) < p) or (n != m + p)
print(f"Outra Expressão Relacional: {outra_expressao_relacional}") 


'''
EXERCÍCIOS:

Executar expressões matemáticas:

Defina as variáveis a = 7, b = 3, c = 5, d = 2
Execute a expressão matemática complexa:
((a * b) + (c / d)) - (a ** b)
Anote o resultado

'''

a,b,c,d = 7,3,5,2

expressao_matematica = ((a * b) + (c / d)) - (a ** b)
print(f"Resultado da expressão matemática: {expressao_matematica}")


'''
Análisar de expressões condicionais:

Defina as variáveis x = 10, y = 20, z = 30
Execute a expressão condicional:
(x < y and y > z) or (x + y == z and not (z == x * 3))
Determine se a expressão retorna True ou False

'''

x,y,z = 10,20,30

expressao_condicional = (x < y and y > z) or (x + y == z and not (z == x * 3))
print(f"Resultado da expressão condicional: {expressao_condicional}")

expressao_condicional2 = (x < y and y > z) or (x + y == z and (z == x * 3))
print(f"Resultado da expressão condicional 2: {expressao_condicional2}")


'''
Criar e Executar Expressões Relacionais:

Defina as variáveis m = 25, n = 35, p = 45
Crie uma expressão relacional que combine operadores matemáticos, lógicos e de comparação
Execute a expressão:
((m + n) > (p * 2)) and ((p / n) < m) or (n == m + p)
Anote o resultado

'''

m = 25
n = 35  
p = 45

expressao_relacional = ((m + n) > (p * 2)) and ((p / n) < m) or (n == m + p)
print(f"Resultado da expressão relacional: {expressao_relacional}")

expressao_relacional2 = ((m + n) > (p * 2)) and ((p / n) < m) or (n < m + p)
print(f"Resultado da expressão relacional 2: {expressao_relacional2}")