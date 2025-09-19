print("Menu de Cadastro")
print("1 - Cadastrar aluno")
print("2 - Listar alunos")
print("3 - Pesquisa por nome do aluno")
print("4- Sair")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("Você escolheu a opção: Cadastrar aluno")
    input("Digite o nome do aluno: ")
    input("Digite a idade do aluno: ")
    input("Digite o curso do aluno: ")
    print("Aluno cadastrado com sucesso!")

elif opcao == 2:
    print("Você escolheu a opção: Listar alunos")
    print("Lista de alunos:")
    print("1. Ana , 20 anos, Nutrição")
    print("2. Manu , 22 anos, Biologia")
    print("3. Sophia, 20 anos, Química")

elif opcao == 3:
    print("Você escolheu a opção: Pesquisa por nome do aluno")
    input("Digite o nome do aluno que deseja pesquisar: ")
    print("Aluno encontrado!")

elif opcao == 4:
    print("Você escolheu a opção: Sair")
    print("Saindo do sistema...")

else:
    print("Opção inválida! Tente novamente.")
   