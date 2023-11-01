print("Olá, morador!")
while True:
    bloco = int(input("Digite o número do bloco que você mora: "))
    if 1 <= bloco <= 10: 
        print("O Sr. José administra seu bloco.")
        break
    elif 11 <= bloco <= 20: 
        print("O Sr. Hamilton administra seu bloco.")
        break
    else:
        resposta = input("Este bloco não existe. Deseja tentar novamente? (SIM ou NÃO): ")
        if resposta.upper() != "SIM":
            break
print("Ficamos à disposição.")