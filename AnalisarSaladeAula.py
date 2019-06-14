from funcoesProjeto import *
from os import listdir, system

while True:
    try:
        print(f"""O que deseja fazer?
        [ 1 ] Gerar informações da turma.
        [ 2 ] Exibir arquivos disponíveis.
        [ 3 ] Analisar arquivo da turma.
        [ 4 ] SAIR""")
        acao = int(input())

        # COMANDO GERAR BASE DE DADOS
        if acao == 1:
            nome = input("Informe o nome do arquivo a ser criado: ").strip()
            while nome == "":
                nome = input("Informe o nome do arquivo a ser criado: ").strip()
            gerarturma(nome)

        # COMANDO EXIBIR ARQUIVOS .TXT
        elif acao == 2:
            items = listdir("./")
            arquivos_txt = []
            for item in items:
                if item.endswith(".txt"):
                    arquivos_txt.append(item)
            if len(arquivos_txt):
                print("-=-" * 30)
                print(f"Lista de arquivos encontrados: ", end=" ")
                for x in range(len(arquivos_txt)):
                    if x == len(arquivos_txt) - 1:
                        print(arquivos_txt[x])
                    else:
                        print(arquivos_txt[x], end=" | ")
                print("-=-" * 30)
            else:
                print("Não foram encontrados arquivos .TXT")

        # COMANDO ANALISAR BASE DE DADOS
        elif acao == 3:
            while True:
                try:
                    arquivo_entrada = input("Informe o arquivo a ser analisado [com formato]: ").strip().lower()
                    arquivo_entrada = open(arquivo_entrada, encoding="UTF-8")
                    break
                except:
                    print("Arquivo não localizado.")

            arquivo_saida = input(
                "Informe o nome do arquivo onde serão salvas as informações [sem formato]: ").strip().lower()
            while True:
                try:
                    print("""Informe o formato do arquivo que deverá ser criado:
                    [ 1 ] Formato [.txt]
                    [ 2 ] Formato [.html]""")
                    formato_saida = int(input())
                    if formato_saida == 1:
                        formato_saida = 'txt'
                        break
                    elif formato_saida == 2:
                        formato_saida = 'html'
                        break
                    else:
                        print("Formato inválido.")
                except:
                    print("Formato inválido.")
                    continue
            analisarturma(arquivo_saida, formato_saida, arquivo_entrada)

        # COMANDO SAIR
        elif acao == 4:
            print("Aplicação encerrada.")
            system("PAUSE")
            break
        else:
            print("Ação inválida.")
    except:
        continue
