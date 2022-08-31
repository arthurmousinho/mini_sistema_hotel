import os

quartos_disponiveis = [401, 402, 403, 404, 405, 406, 407, 408, 409, 410]
estoque_produtos = ["Água Mineral sem gás 500ml", "Refrigerante", "Cholocate em barra", "Água com Gás 500ml", "Barra de Cereal", "Amendoim "]
valor_produtos = [3.00, 5.00, 2.50, 3.50, 1.50, 4.00]

quartos_ocupados = []
clientes = []
produtos_consumidos = ["","","","","","","","",""]
valor_produtos_consumidos = [0,0,0,0,0,0,0,0,0,0]

def limpa():
    os.system('cls')


def menu_principal():
        print('''


    -----------------------------------------------------------------                            
    |                    H O T E L   P Y T H O N                    |
    |                                                               |
    |    [1] Check-in de clientes                                   |
    |    [2] Consumação no hotel                                    |
    |    [3] Adicionar produtos para a consumação dos clientes      |
    |    [4] Check-out de clientes                                  |
    |    [5] Ver clientes que estão hospedados                      |
    |                                                               |
    -----------------------------------------------------------------


    ''')


while True:
    menu_principal()
    
    try:
        opcao = int(input("> "))
    except(ValueError,TypeError):
        print("Tente novamente")
        limpa()
        continue
    else:
        if opcao > 5 or opcao < 1:
            print("Opção inválida")


        elif opcao == 1: # Check-in de clientes
            if len(quartos_disponiveis) == 0:
                limpa()
                print("Hotel está lotado") 
                continue
            else:

                limpa()
                while True:
                    try: 
                        nome = str(input("Nome do hospede: ")) 
                        if nome in clientes:
                            print("Tem um cliente com esse mesmo nome, tente novamente") 
                            continue
                        else:
                            clientes.append(nome) 
                    except(TypeError,ValueError):
                        print("Tente novamente")
                        continue
                    else:
                        while True:
                            limpa()

                            print("Quartos disponíveis")
                            for e in quartos_disponiveis:
                                print(f'''
                                        [{e}]
                                ''')
                            
                            try:
                                quarto_escolhido = int(input("Digite o número do quarto que o cliente vai ser hospedado: "))
                            except(ValueError,TypeError):
                                limpa()
                                print("Tente novamente")
                                continue
                            else:
                                if quarto_escolhido not in quartos_disponiveis:
                                    limpa()
                                    print("Quarto escolhido não está disponível, escolha outro quarto")
                                    continue
                                else:
                                    limpa()
                                    print(f"{nome} está hospedado no quarto {quarto_escolhido}")  
                                    quartos_ocupados.append(quarto_escolhido)
                                    del quartos_disponiveis[quartos_disponiveis.index(quarto_escolhido)]
                            break
                    break      


        elif opcao == 2: # Consumação no hotel    
            while True:
                try:
                    numero_quarto = int(input("Qual quarto está fazendo o pedido? > "))
                except(ValueError,TypeError):
                    limpa()
                    print("Tente novamente")
                    continue
                else:
                    if numero_quarto not in quartos_ocupados:
                        limpa()
                        print("Quarto está sem hospede, tente novamente")
                        continue
                    else:
                        while True:
                                print("Produtos: ")
                                i = 0
                                while i < len(estoque_produtos):
                                    print(f'''
                                        [{i+1}]   {estoque_produtos[i]} >> R$ {valor_produtos[i]}
                                    ''')
                                    i = i + 1
                                try:
                                    escolha_produto = int(input("Digite o índice do produto desejado > "))
                                except(ValueError,TypeError):
                                    limpa()
                                    print("Tente novamente")
                                    continue
                                else:
                                    if escolha_produto > len(estoque_produtos):
                                        limpa()
                                        print("Tente novamente")
                                        continue
                                    else:
                                        limpa()

                                        posicao = quartos_ocupados.index(numero_quarto)
                                        produtos_consumidos[posicao] = estoque_produtos[escolha_produto - 1]            
                                        valor_produtos_consumidos[posicao] = valor_produtos_consumidos[posicao] + valor_produtos[escolha_produto - 1]

                                        limpa()
                                        print(f'''
                                            PRODUTO {estoque_produtos[escolha_produto - 1]} 
                                            VALOR: R$ {valor_produtos[escolha_produto - 1]}
                                            CLIENTE: {clientes[quartos_ocupados.index(numero_quarto)]}
                                        ''')
                                        break
                        break


        elif opcao == 3: # Adicionar produtos para a consumação dos clientes 
            pass
            while True:
                try:
                    nome_novo_produto = str(input("Nome do novo produto: "))
                    valor_novo_produto = float(input("Valor do novo produto: R$ "))
                except(ValueError,TypeError):
                    limpa()
                    print("Tente novamente")
                    continue
                else: 
                    if nome_novo_produto in estoque_produtos:
                        limpa()
                        print("Tem um produto com o mesmo nome cadastrado no sistema, tente outro nome")
                        continue
                    else:
                        limpa()
                        estoque_produtos.append(nome_novo_produto)
                        valor_produtos.append(valor_novo_produto)
                        print(f"Produto {nome_novo_produto} com valor de R$ {valor_novo_produto} adicionado com sucesso")

                    
                        try: 
                            add_ou_cancelar = int(input("[1] ADCIONAR MAIS PRODUTOS         [2] FINALIZAR CADASTRO DO PRODUTOS "))
                        except(ValueError,TypeError):
                            limpa()
                            print("Tente novamente")
                            continue
                        else:
                            while add_ou_cancelar < 1 or add_ou_cancelar > 2:
                                try: 
                                    add_ou_cancelar = int(input("[1] ADCIONAR MAIS PRODUTOS         [2] FINALIZAR CADASTRO DO PRODUTOS "))
                                except(ValueError,TypeError):
                                    limpa()
                                    print("Tente novamente")
                                    continue
                            if add_ou_cancelar == 1:
                                limpa()
                                continue
                            elif add_ou_cancelar == 2:
                                limpa()
                                break


        elif opcao == 4: # Check-out de clientes 
            while True:
                try:
                    nome_cliente = str(input("Nome do cliente hospedado: "))
                    numero_quarto = int(input("Número do quarto que o cliente estava hospedado: "))
                    qtd_dias = int(input("Quantos dias o cliente ficou hospedado: "))
                except(ValueError,TypeError):
                    limpa()
                    print('Tente novamente')
                    continue
                else: 
                    if nome_cliente not in clientes:
                        limpa()
                        print("Cliente não encontrado, tente novamente")
                        continue
                    elif numero_quarto not in quartos_ocupados:
                        limpa()
                        print("Quarto não possui cliente hospedado, tente novamente")
                        continue
                    elif quartos_ocupados.index(numero_quarto) != clientes.index(nome_cliente):
                        limpa()
                        print("Nesse quarto possui outro cliente, tente novamente")
                        continue
                    else:
                        while True:
                            print(f'''
                                HOSPEDAGEM = R$ {qtd_dias * 100}                [R$ 100 por dia]
                                CONSUMO DE PRODUTOS = R$ {valor_produtos_consumidos[quartos_ocupados.index(numero_quarto)]}
                                -----------------------------------------------------------------
                                                    TOTAL: R$ {qtd_dias * 100 + valor_produtos_consumidos[quartos_ocupados.index(numero_quarto)]}
                            ''')

                            try:
                                checkout_hospede = int(input("[1] DESPACHAR CLIENTE     [2] CANCELAR DESPACHO"))
                            except(ValueError,TypeError):
                                limpa()
                                print("Tente novamente")
                                continue
                            else: 
                                if checkout_hospede < 1 or checkout_hospede > 2:
                                    limpa()
                                    print("Tente novamente")
                                    continue
                                elif checkout_hospede == 1:
                                    posicao = clientes.index(nome_cliente)


                                    del quartos_ocupados[posicao]
                                    del clientes[posicao]
                                    del valor_produtos_consumidos[posicao]

                                    quartos_disponiveis.append(numero_quarto)

                                    limpa()
                                    print(f"Cliente {nome_cliente} fez o check-out com sucesso")
                                    break
                                elif checkout_hospede == 2:
                                    limpa()
                                    print("Checkout cancelado")
                                    break
                    break  


        elif opcao == 5:
            while True:
                print("Clientes hospedados no hotel")
                j = 0
                while j < len(quartos_ocupados):
                    print(f'''
                            [{quartos_ocupados[j]}]                 {clientes[j]}
                    ''')
                    j = j + 1
                try:
                    sair = int(input("[1] PARA SAIR"))
                except(ValueError,TypeError):
                    limpa()
                    print("Tente novamente")
                    continue
                else:
                    if sair != 1:
                        limpa()
                        print("Opção inválida")
                        continue
                    else:
                        limpa()
                        break




# Developed by @arthurmousinho
