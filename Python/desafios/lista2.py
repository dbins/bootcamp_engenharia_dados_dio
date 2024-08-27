def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        if count > max_count:
            max_count = count
            max_produto = produto
        
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    lista_entrada = entrada.split(", ")
    produtos = list(map(lambda x: x.strip(), lista_entrada))
    return produtos

produtos = obter_entrada_produtos()
mais_vendido = produto_mais_vendido(produtos)
print(mais_vendido)