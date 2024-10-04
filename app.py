usuarios = []

while True:
    print("\nMenu:")
    print("1. Cadastrar usuário")
    print("2. Exibir usuários cadastrados")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    match escolha:
        case '1':
            nome = input("Digite o nome do usuário: ")
            idade = input("Digite a idade do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            profissao = input("Digite a profissão do usuário: ")
            tipo_sanguineo = input("Digite o tipo sanguíneo do usuário: ")
            peso = input("Digite o peso do usuário (kg): ")
            altura = input("Digite a altura do usuário (m): ")

            usuario = {
                "Nome": nome,
                "Idade": idade,
                "CPF": cpf,
                "E-mail": email,
                "Profissão": profissao,
                "Tipo Sanguíneo": tipo_sanguineo,
                "Peso": peso,
                "Altura": altura
            }

            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso!")

        case '2':
            print("\nUsuários cadastrados:")
            for usuario in usuarios:
                print("-" * 40)
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                print("-" * 40)

        case '3':
            print("Saindo do programa.")
            break

        case _:
            print("Opção inválida! Tente novamente.")
