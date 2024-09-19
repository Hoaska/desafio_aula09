lista = []
while True:
    print(30*'*', 'Menu', 30*'*')
    print('1. Cadastrar produto ')
    print('2. Listar produtos ')
    print('3. remover produto ')
    print('4. sair da operação ')
    print(66*'*')

    opcao = input('Digite a opção escolhida: ')
    if opcao == '1':
        produto = input('Insira o produto a ser adicionado: ')
        valor = float(input(f'Valor do {produto}: '))
        quant = float(input(f'Quantidade do {produto}: '))
        soma = float((valor * quant))
        valort = (soma)
        lista.append(f'produto: {produto}, valor: {valor}, quantidade: {quant}, custo total: {valort}')
        pass
    elif opcao == '2':
        if len(lista) == 0:
            print('Lista vazia!')
        else:
            print('Produtos na lista: ')
            for produto in lista:
                print(f'Nome: {produto}, Quantidade: {quant}, Valor: {valor}')
        pass
    elif opcao == '3':
        produto = input('Produto a ser excluido: ')
        for produto in lista:
            if produto in lista:
                lista.pop()
                print('Produto excluído! ')
                pass
    elif opcao == '4':
        print('Fim da operação.')
        break