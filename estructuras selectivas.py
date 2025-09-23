mxn = float(input("Ingrese la cantidad en pesos:"))
opcion = int(input("Selecciona la opcion:"))
match opcion:
    case 1:
        print(mxn*0.058,"USD")
    case 2:
        print(mxn*0.053,"EUR")
    case 3:
        print(mxn*8.56,"JPY")
    case 4:
        print(mxn*0.045,"GBP")
    case _:
        print()