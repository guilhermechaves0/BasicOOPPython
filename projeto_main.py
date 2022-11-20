import random

class Produtos:
    
    
    def __init__(self, product, quantity, price):
        self.product = str(product)
        self.quantity = int(quantity)
        self.price = float(price)
    
    #   Testando a inserir coisas a lista
    produtos = []
    produtos.append('Maçã', 10, 2.58)
    produtos.append('Laranja', 10, 5.98)
    produtos.append('Manga', 10, 4.23)
    
    def verifica_list(list_cliente, list_product):
        for i in list_cliente:
            if(list_cliente[i] == list_cliente[i]):
                print(list_product[i])
        
def add(aux):
    pass

def remove():
    pass

def finish():
    pass

def cancel():
    print("\nSua compra foi cancelada! Obrigado por nos visitar, até a próxima!\n")

def add_product(list, product):
    list = []
    quantity = 15
    price = random.uniform(2, 9.9)
    list.append(Produtos(product, quantity, price))

def menu_principal(list):
    x = True
    while x == True:
        option = int(input("Escolha uma opção (numero inteiro):\n0 ➙ CANCEL;\n1 ➙ ADD;\n2 ➙ REMOVE;\n3 ➙ FINISH.\nPor favor, insira o código: "))
        match option:
            case 0:
                cancel()
                x = False
            case 1:
                add()
                pass
            case 2:
                remove()
                pass
            case 3:
                finish()
                x = False
            case 4:
                #   Adicionar produtos
                add_product(list, produto = input("Digite o nome do produto a ser adicionado: "))
                pass
            case default:
                print("\nCódigo inválido! Por favor, insira o código correspondente.\n")
                pass
            
def main():
    listCliente = []
    print("Bem-vindo a LearnStore!")
    menu_principal(listCliente)
    
    
    for i in produtos:
        print(i.product, i.quantity, i.price)


if __name__ == "__main__":
    main()
