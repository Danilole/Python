def pessoa(nome, idade=None):
    print(f'Nome:   {nome}')
    if idade != None:
        print(f'Idade:  {idade} anos')
    else:
        print("Idade não informada.")

pessoa('Danilo',37)