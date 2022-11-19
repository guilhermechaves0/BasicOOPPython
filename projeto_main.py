def main():
    print("Bem-vindo a LearnStore!")
def add():
    pass

def remove():
    pass

def finish():
    pass

def cancel():
    pass


def menu_principal():
    x = True
    while x == True:
        option = int(input("Escolha uma opção: 0 ➙ Cancel, 1 ➙ ADD, 2 ➙ REMOVE, 3 ➙ FINISH\n"))
        match option:
            case 0:
                cancel()
                x = False
            case 1:
                add()
            case 2:
                remove()
            case 3:
                finish()

if __name__ == "__main__":
    main()
    menu_principal()
