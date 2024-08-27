def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    total_elementos = len(vendas)
    media_vendas = total_vendas / total_elementos
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    lista_entrada = entrada.split(", ")
    vendas = list(map(int, lista_entrada))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))