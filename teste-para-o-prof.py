import math

def calculadora_avancada():
    print("1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Potência, 6 - Raiz Quadrada")
    escolha = input("Escolha a operação (1-6): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if escolha == '1': print("Resultado:", num1 + num2)
        elif escolha == '2': print("Resultado:", num1 - num2)
        elif escolha == '3': print("Resultado:", num1 * num2)
        elif escolha == '4': print("Resultado:", num1 / num2 if num2 != 0 else "Erro: Divisão por zero")
    elif escolha == '5':
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        print("Resultado:", math.pow(base, expoente))
    elif escolha == '6':
        num = float(input("Digite o número: "))
        print("Resultado:", math.sqrt(num))
    else:
        print("Opção inválida")

# Chamada da função 
calculadora_avancada()