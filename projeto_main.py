class Produtos:

    def __init__(self, product, quantity, price):
        self.product = str(product)
        self.quantity = int(quantity)
        self.price = float(price)

def main():
    print("Bem-vindo a LearnStore!")
    #   menu_principal()
    
    #   Testando a inserir coisas a lista
    produtos = []
    produtos.append(Produtos('Maçã', 10, 2.58))
    produtos.append(Produtos('Laranja', 10, 5.98))
    produtos.append(Produtos('Manga', 10, 4.23))
    
    for i in produtos:
        print(i.product, i.quantity, i.price)

def add(aux):
    pass

def remove():
    pass

def finish():
    pass

def cancel():
    print("\nSua compra foi cancelada! Obrigado por nos visitar, até a próxima!\n")

def menu_principal():
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
            case default:
                print("\nCódigo inválido! Por favor, insira o código correspondente.\n")
                pass

if __name__ == "__main__":
    main()
