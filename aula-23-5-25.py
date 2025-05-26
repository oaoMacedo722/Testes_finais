clinames=[]
opc = 0 

while True: 
    print("1 - inserir nome do cliente: ")
    print("2 - Listar clientes")
    print("3 - Sair")
    opc = input("Insert option: ")
    match opc: 
        case '1' :
            clinames.append(input("insert nome cli: "))
        case '2' : 
            for cliname in clinames: 
                print(cliname)
        case '3' : 
            print("Adius muxaxos")
            break
        case default: 
            print("opc nao existe")