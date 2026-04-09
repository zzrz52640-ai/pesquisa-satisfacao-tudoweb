print("=" * 60)
print("          PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("          Atendimento ao Cliente")
print("=" * 60)

# Contadores
excelente = 0
ruim = 0

# Loop FOR para 50 entrevistados
for i in range(1, 51):
    print(f"\n--- Entrevistado {i} de 50 ---")
    
    nome = input("Digite o nome do entrevistado: ").strip()
    
    # Validação simples da idade
    while True:
        try:
            idade = int(input("Digite a idade (apenas números): "))
            if idade < 0 or idade > 120:
                print("Idade inválida! Digite uma idade entre 0 e 120.")
            else:
                break
        except ValueError:
            print("Por favor, digite apenas números para a idade.")
    
    # Opinião/ estrutura
    while True:
        print("\nOpinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        try:
            opiniao = int(input("Escolha uma opção (1/2/3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite apenas o número da opção.")
    
    # Contagem usando estruturas de decisão
    if opiniao == 1:
        excelente += 1
        print(f"{nome} avaliou como EXCELENTE ✓")
    elif opiniao == 3:
        ruim += 1
        print(f"{nome} avaliou como RUIM ✗")
    else:
        print(f"{nome} avaliou como BOM")

# Resultados finais sendo esses
print("\n" + "=" * 60)
print("          RESULTADO DA PESQUISA - TUDOWEB")
print("=" * 60)
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM:      {ruim}")
print(f"Total de entrevistados:           50")
print("=" * 60)
