# Define a função que realiza a operação de soma
def soma(a, b):
    return a + b

# Define a função que realiza a operação de subtração
def subtracao(a, b):
    return a - b

# Define a função que realiza a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Define a função que realiza a operação de divisão
def divisao(a, b):
    return a / b

# Exibe o menu de opções da calculadora
print("Selecione a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Lê a opção escolhida pelo usuário
opcao = int(input("Digite sua opção (1/2/3/4): "))

# Lê os dois números para realizar a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida pelo usuário
if opcao == 1:
    resultado = soma(num1, num2)
elif opcao == 2:
    resultado = subtracao(num1, num2)
elif opcao == 3:
    resultado = multiplicacao(num1, num2)
elif opcao == 4:
    resultado = divisao(num1, num2)
else:
    print("Opção inválida!")

# Exibe o resultado da operação
print("O resultado é:", resultado)
