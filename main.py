# Qualificação de candidato Estágio de desenvolvimento - Oak Tecnologia

# Autor: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

import os

productList = []

# FUNÇÃO PARA ADICIONAR PRODUTOS
def addProduct():
    os.system("cls")
    productTemp = {}
    
    print("----------------")
    print("  NOVO PRODUTO  ")
    print("----------------")
    print("1. Inserir nome do produto: ")
    productTemp["name"] = input()
    print("2. Inserir descrição do produto: ")
    productTemp["description"] = input()
    print("3. Inserir valor do produto: ")
    productTemp["price"] = float(input())
    
    loop = True
    availabilityTemp = ""
    
    while loop:
        print("5. Esse produto está disponível? [s/n]")
        print("(s = produto disponível   n = produto indisponível)")
        availabilityTemp = input()
        
        if ((availabilityTemp == "s") or (availabilityTemp == "n")):
            loop = False
            productTemp["availability"] = True if (availabilityTemp == "s") else False
        else:
            print("### Erro! Opção inválida.")
            
    productList.append(productTemp)
    listProducts()

# FUNÇÃO PARA LISTAR PRODUTOS
def listProducts():
    os.system("cls")
    print("-------------------------")
    print(" NOME\t|\tVALOR")
    print("-------------------------")
    
    productListAscending = sorted(productList, key=lambda x: x['price'])
    
    for index, product in enumerate(productListAscending):
        print(index+1,". ",product["name"],"\tR$",format(product["price"],".2f"))
        
    print("----------------")
    print("Cadastrar outro produto? [s/n]")
    print("(s = cadastrar outro produto   n = voltar ao menu)")
    option = input()
    
    if (option == "s"):
        addProduct()
    else:
        menu()

# FUNÇÃO PRINCIPAL
def menu():
    os.system("cls")
    loop = True

    while loop:
        print("----------------")
        print("     MENU")
        print("----------------")
        print(" [1] Adicionar produto")
        print(" [2] Listar produtos")
        print(" [3] Sair")

        option = int(input())

        if ((option >= 1) and (option <= 3)):
            loop = False
        else:
            os.system("cls")
            print("### Erro! Opção inválida.")

        if (option == 1):
            addProduct()

        if (option == 2):
            listProducts()

menu()
