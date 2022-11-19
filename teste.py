x = True
y = int(input("Por favor, insira um código válido: "))
while x == True:
    match y:
        case 0:
            print(f"Seu código {y} é quase lá!")
            y = int(input("Por favor, insira um código válido: "))
        case 1:
            print("Works! Saímos do loop!")
            x = False 
