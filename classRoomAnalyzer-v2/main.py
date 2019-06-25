from functions import *
from os import system, path


while True:
    # MENU
    print("=" * 40)
    print(f"""{'CLASSROOM ANALYZER':^40}
    [ 1 ] Exibir arquivos DATABASE.
    [ 2 ] Gerar turma aleatória.
    [ 3 ] Cadastrar novo aluno.
    [ 4 ] Atualizar base de dados.
    [ 5 ] Analisar base de dados.
    [ 6 ] Exibir arquivos ANALISE.
    [ 7 ] ENCERRAR APLICAÇÃO.""")
    print("=" * 40)
    opcao = input("Informe sua opção: ")
    if opcao == "1":
        exibirdb()
        arquivosdb = listardb()
        if len(arquivosdb) != 0:
            arq = input("Selecione o arquivo a ser exibido: ").strip()
            while not arq.isnumeric():
                arq = input("Selecione o arquivo a ser exibido: ").strip()
            arquivo = "./database/" + arquivosdb[int(arq)]
            webbrowser.open(path.abspath(arquivo))
            # system(f"notepad {path.abspath(arquivo)}")
    elif opcao == "2":
        turmaaleatoria()
    elif opcao == "3":
        criaraluno()
    elif opcao == "4":
        alterarbasedados()
    elif opcao == "5":
        exibirdb()
        listasdb = listardb()
        if len(listasdb) != 0:
            db = input("Informe a database que deseja analisar: ")
            while (not db.isnumeric()) or (int(db) <= 0) or (int(db) > len(listasdb)):
                print("[ERRO] ENTRADA INVÁLIDA.")
                db = input("Informe a database que deseja analisar: ")
            db = int(db)
            db = listasdb[db]
            analisar(db)
    elif opcao == "6":
        exibiranalises()
    elif opcao == "7":
        print("Aplicação encerrada...")
        system("PAUSE")
        break
    else:
        print("[ERRO] OPÇÃO INVÁLIDA.")
