#Código sem função

fluxo_caixa = []

print("_____________")
print("@ fluxo de caixa")
print("_____________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")

#Função adicionar e retirar
def adicionar_transacao():
     nome = ( input("Nome: ") )
     valor = float( input("Valor: ") )
     fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

while True:

    opcao = int( input("Digite a opção: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

#Notafiscal
total = 0
for fc in fluxo_caixa:
    print("Nome: ", fc['nome'], "Valor: R$", fc['valor'])
    total = total + fc['valor']

print("Saldo atual: R$", total)