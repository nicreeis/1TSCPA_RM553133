titulo = "Programa de Recompensa por tarefa"
print(f'{titulo:^30}')
dia_da_semana = input("Hoje é sexta-feira? (Digite SIM ou NÃO): ").upper()
if dia_da_semana == "SIM":
    lavar_sniff = input("Você deu banho no Sniff? (Digite SIM ou NÃO): ").upper()
    dever_de_casa = input("Você fez o dever de casa? (Digite SIM ou NÃO): ").upper()
    if dever_de_casa == "SIM" and lavar_sniff == "SIM":
        print("Vamos tomar sorvete na DAMP!")
    elif dever_de_casa == "SIM" and lavar_sniff == "NÃO":
        print("Precisa dar banho no Sniff para irmos tomar sorvete na DAMP.")
    elif dever_de_casa == "NÃO" and lavar_sniff == "SIM":
        print("Precisa fazer o dever de casa para irmos tomar sorvete na DAMP.")
    else:
        print("Não vamos tomar sorvete na DAMP :(")
else:
    print("Hoje não é dia de completar as tarefas e ir tomar sorvete.")