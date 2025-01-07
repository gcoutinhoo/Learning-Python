entrada = input("Digite os números: ")

numeros = list(map(int, entrada.split()))
soma = sum(numeros)
numeros_invertidos = numeros[::-1]

print("Lista invertida:", numeros_invertidos)
print("Soma dos números:", soma)
