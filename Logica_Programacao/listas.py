lista_feira =  ["maça", "bananaa", "morango"]

print(lista_feira[2])

#add na lista
lista_feira.append(input("digite a fruta que você precisa: "))

#insere no indice indicado
lista_feira.insert(0, "abacaxi")


for fruta in lista_feira:
    print("\n", fruta)
    
#remover item da lista 
lista_feira.pop()

print(lista_feira)


#remove por nome ou string
lista_feira.remove("maça")