def maiorNumero(a, b, c):
    return max(a, b, c)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = maiorNumero(num1, num2, num3)
print(f"O maior número é: {maior}")