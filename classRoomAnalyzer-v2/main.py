from functions import *
from os import system


while True:
    # MENU
    print("=" * 40)
    print(f"""{'CLASSROOM ANALYZER':^40}
    [ 1 ] Exibir arquivos DATABASE.
    [ 2 ] Gerar turma aleatória.
    [ 3 ] Cadastrar novo aluno.
    [ 4 ] Atualizar base de dados.
    [ 5 ] Exibir arquivos ANALISE.
    [ 6 ] ENCERRAR APLICAÇÃO.""")
    print("=" * 40)
    opcao = input("Informe sua opção: ")
    if opcao == "1":
        exibirdb()
    elif opcao == "2":
        turmaaleatoria()
    elif opcao == "3":
        criaraluno()
    elif opcao == "4":
        alterarbasedados()
    elif opcao == "5":
        exibiranalises()
    elif opcao == "6":
        print("Aplicação encerrada...")
        system("PAUSE")
        break
    else:
        print("[ERRO] OPÇÃO INVÁLIDA.")
