#exercicio: Uma empresa faz desconto caso o valor total da compra seja maior que 100
# e se for pago no pix

nome = input("qual seu nome: ")
total = float(input("por favor, informe o total da compra: "))
forma = input("qual foi a forma de pagamento: \n1 - para cartão\n2 - para dinheiro\n3 - para pix\nescolha um:")

#len para contar caracteres da var nome
#print(len(nome))

nomel = len(nome)
if nomel < 3 :
    print(f"o seu nome deve conter no minímo 3 caracteres {nome} {nomel}")
elif total > 100 and forma == "pix" or forma == "3":
    print("o cliente tem direito ao desconto")
else:
    print("o cliente não tem direito ao desconto")