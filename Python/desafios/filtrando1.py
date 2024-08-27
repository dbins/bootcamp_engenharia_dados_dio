def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    visuais = [i.title() for i in visuais]
    lista_sem_duplicados = set(visuais)
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = sorted(list(set(lista_sem_duplicados)))
     
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)