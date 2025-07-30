def menu():

    menu = """
    [d] -> Depositar
    [s] -> Sacar
    [e] -> Extrato
    [v] -> Sair
    [nu] -> Novo usuário
    [nc] -> Nova conta
    [lc] -> Listar contas

"""
    return input(menu)

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato = f"Depósito realizado no valor R$ {valor:.2f}\n"
        return valor,extrato
    else:
        print("Falha na operação. O valor informado é inválido")
        return 0


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Não há saldo suficiente na conta.")
    elif valor > limite:
        print("Falha na operação. Não é possível sacar mais que 500 reais por dia.")
    elif numero_saques > limite_saques:
        print("Falha na operação. O número de saques excedeu o limite.")
    elif valor > 0:
        saldo -= valor
        numero_saques +=1
        extrato = f"Saque realizado no valor R$ {valor:.2f}\n"
    else:
        print("Falha na operação. O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print("=============EXTRATO============")
        print(f"Saldo R$ {saldo:.2f}")
        print("----------------------------------")

def criar_usuario(usuarios):
    user = dict()
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuarios(cpf,usuarios)
    if usuario:
        print("Usuário já existe")
        return
    user["cpf"] = cpf
    nome = input("Informe o nome do usuário:")
    user["nome"] = nome
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    user["data_nascimento"] = data_nasc
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    user["endereco"] = endereco
    usuarios.append(user)
    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf,usuarios):
    for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return usuario 
            else:
                return None
                
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf da conta a ser criada: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario": usuario}
    else:
        print("Não foi possível cadastrar a conta pois o usuário não existe.")

def listar_contas(contas):
    for conta in contas:
        print(f"{conta} \n")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao=="d":
            valor = float(input("Informe o valor do depósito:"))
            
            saldo, extrato = depositar(saldo,valor,extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado:"))

            saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,
                                   numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
                listar_contas(contas)
                
        elif opcao == "v":
            break

        else:
            print("Operação inválida, tente novamente.")
            

main()