from datetime import datetime

def saudacao():
    
    hora = datetime.now().hour

    if hora < 12:
        print('BOM DIA!')
    elif hora < 18:
        print('BOA TARDE!')
    else:
        print('BOA NOITE!')

def login():

    tentativas = 3

    while tentativas > 0:
    
    
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite sua senha: ")

        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso!")
            break
        
        else:
            tentativas -= 1
            print("Usuário ou senha estão incorretos!")
            print("Tentativas restantes", tentativas)

        if tentativas == 0:
            print("Acesso bloqueado")
            

saudacao()

while True:
            print("\n===== MENU =====")
            print("1 - Fazer login")
            print("2 - Cadastrar usuário")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao =="1":
                login()

            elif opcao =="2":
                print("Cadastro de usuário em construção")

            elif opcao =="3":
                print("Saindo do sistema")
                break

            else:
               print("Opção inválida")
               
            
        
login()