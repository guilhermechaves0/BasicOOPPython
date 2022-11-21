class Produto:
    def __init__(self, id, name, price, quant) -> None:
        self.id = int(id)
        self.name = str(name)
        self.price = float(price)
        self.quant = int(quant)

    def remove_item(self):
        if(self.quant):
            self.quant-=1
        else:
            return("")

class Loja:
    def __init__(self) -> None:
        pass

    def iniciando_produtos(self) -> None:
        inic_prod = [
            Produto(1, "Camisa Preta", 34.99, 4),
            Produto(2, "Camisa Branca", 29.99, 3),
            Produto(3, "Cueca Básica", 19.99, 10),
            Produto(4, "Cueca Premium", 99.99, 7)
        ]

        return inic_prod

def menu_principal():
    x = True
    while x == True:
        option = int(input("Escolha uma opção (numero inteiro):\n0 ➙ CANCEL;\n1 ➙ ADD;\n2 ➙ REMOVE;\n3 ➙ FINISH.\nPor favor, insira o código: "))
        match option:
            case 0:
                x = False
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                x = False
                pass
            case default:
                print("\nCódigo inválido! Por favor, insira o código correspondente.\n")
                pass

def main():
    print("Bem-vindo a LearnStore!")
    menu_principal()

if __name__ == "__main__":
    main()
