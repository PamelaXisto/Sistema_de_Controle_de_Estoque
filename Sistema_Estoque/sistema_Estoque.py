produtos = []
estoques = []
opcao = 0

print('-_' * 15, '< BEM VINDO A LOJA DE ELETRÔNICOS! >', '-_' * 15)

while opcao != 4:
  print('Vamos às compras ?! ')
  print('Escolha uma opção do MENU:')
  
  print('-=' * 15)

  print('''  [1] - Adicionar produto
  [2] - Atualizar produto
  [3] - Visualizar estoque disponível
  [4] - Sair do programa''')
  
  print('-=' * 15)
  
  opcao = int(input('Digite a opção: '))
  if opcao == 1:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto R$ '))
    quantidade = int(input('Digite a quantidade em estoque: '))
    produtos.append(produto)
    estoques.append([preco, quantidade])
    print('Produto adicionado na lista com sucesso!')

  elif opcao == 2:
    produto = input('Digite o nome do produto: ')
    if produto in produtos:
      preco = float(input('Digite o novo preço para o produto: '))
      quantidade = int(input('Digite a nova quantidade em estoque: '))
      indice = produtos.index(produto)
      estoques[indice] = [preco, quantidade]
      print('Produto atualizado na lista com sucesso!')
    else:
      print('Produto não encontrado!')

  elif opcao == 3:
    print('Estoque:')
    for i in range(len(produtos)):
      print(f'-------|{produtos[i]} no valor de R${estoques[i][0]} reais|-------|contendo {estoques[i][1]} unidades|-------')

  elif opcao == 4:
    print('Você acabou de sair do programa. Volte sempre!')
  else:
    print('Esta opção é inválida, tente novamente nas opções abaixo!')