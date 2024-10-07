def lista_de_compras():
    lista = []
    while True:
        opc = int(input(
            "1 - Adicionar itens\n2 - Remover itens\n3 - exibir lista de itens no carrinho\n4 - Sair\nDigite uma opção: "))

        if opc == 1:
            item = input("Digite o item que deseja comprar: ")
            lista.append(item)
            print(f"{item} foi adicionado à lista com sucesso")

        elif opc == 2:
            nome_remover = input("Escreva o nome do item que deseja remover da lista: ")
            item_encontrado = False
            if not lista:
                print("Nenhum item adicionado")
            else:
                for item in lista:
                    if item == nome_remover:
                        lista.remove(item)
                        item_encontrado = True
                        print("Item removido com sucesso")
                        break
            if not item_encontrado:
                print(f"Item {nome_remover} não foi encontrado.")

        if opc == 3:
            if not lista:
                print("Nenhum item foi adicionado a lista.")
            else:
                for item in lista:
                    print(f"n\ {item}")
