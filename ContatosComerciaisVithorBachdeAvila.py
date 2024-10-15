#Boas-vindas
print("Bem-vindo a lista de contatos de Vithor Bach de Ávila!")

lista_contatos = [] #Lista de dicionarios para armazenar os contatos
id_global = 4978769 #Apresentando meu RU

#Funcao para cadastrar um contato
def cadastrar_contato(id_):
    contato = {}
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")


    #Dicionario para armazenar os dados
    contato["id"] = id_
    contato["nome"] = nome
    contato["atividade"] = atividade
    contato["telefone"] = telefone

    #Copia o dicionario para a lista de contatos
    lista_contatos.append(contato.copy())
    print(f"Contato {nome} cadastrado com sucesso!\n")


#Funcao para consultar contatos
def consultar_contatos():
    while True:
        opcao = input("Escolha a opção de consulta (1. Consultar Todos / 2. Consultar por ID / 3. Consultar por Atividade / 4. Retornar ao Menu): ")

        if opcao == "1": #Consulta todos
            for contato in lista_contatos:
                print(contato)
        elif opcao == "2": #Consulta o ID
            id_ = int(input("Informe o id do contato: "))
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == id_:
                    print(contato)
                    encontrado = True
            if not encontrado:
                print("Id não encontrado.")
        elif opcao == "3": #Consulta por atividade
            atividade = input("informe a atividade: ")
            encontrado = False
            for contato in lista_contatos:
                if contato["atividade"] == atividade:
                    print(contato)
                    encontrado = True
            if not encontrado:
                print("Nenhum contato com esta atividade.")
        elif opcao == "4": #Retorna ao menu
                return
        else:
                print("Opção inválida, tente novamente.")


#Funcao para remover o contato
def remover_contato():
    while True:
        try:
            id_ = int(input("Informe o id do contato para remove-lo: "))
            for contato in lista_contatos:
                if contato["id"] == id_:
                    lista_contatos.remove(contato)
                    print(f"Contato {id_} removido com sucesso!\n")
                    return
            print("Id inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            

#Codigo principal (main)
while True:
    opcao = input("Escolha uma opção (1. Cadastrar Contato / 2. Consultar Contato / 3. Remover Contato 4. Encerrar Programa): ")

    if opcao == "1": #Cadastrar contato
        id_global += 1 #Incrementa o id_global
        cadastrar_contato(id_global) #chama a funcao cadastrar contato
    elif opcao == "2": #Consultar contato
        consultar_contatos()
    elif opcao == "3": #Remover contato
        remover_contato()
    elif opcao == "4": #Encerrar o programa
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida, tente novamente.")