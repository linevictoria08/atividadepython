
funcionarios = []

def menu_principal():
    opcao = 0
    while opcao != 5:
        print("\n Menu principal")
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Calcular Média Salarial")
        print("4 - Analisar Idades")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção (1 a 5): "))

        if opcao == 1:
            cadastrar_funcionario()
        elif opcao == 2:
            listar_funcionarios()
        elif opcao == 3:
            calcular_media_salarial()
        elif opcao == 4:
            analisar_idades()
        elif opcao == 5:
            print("Saindo do sistema. Até a próxima!")
        else:
            print("Opção inválida.")

def cadastrar_funcionario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    salario = float(input("Digite o salário (R$): "))
    funcionario = {"nome": nome, "idade": idade, "salario": salario}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionarios():
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
    else:
        for i, f in enumerate(funcionarios, 1):
            print(f"{i}. Nome: {f['nome']}, Idade: {f['idade']}, Salário: R$ {f['salario']}")

def calcular_media_salarial():
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
    else:
        soma = 0
        for f in funcionarios:
            soma += f["salario"]
        media = soma / len(funcionarios)
        print(f"Média Salarial: R$ {media:.2f}")

def analisar_idades():
    maiores = 0
    menores = 0
    for f in funcionarios:
        if f["idade"] >= 18:
            maiores += 1
        else:
            menores += 1
    print(f"Maiores de idade: {maiores}")
    print(f"Menores de idade: {menores}")

menu_principal()