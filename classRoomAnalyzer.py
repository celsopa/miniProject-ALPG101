from modules.funcoesProjeto import *
from os import system

arquivos_txt = localizartxt()

while True:
    print(f"""CLASSROOM ANALYZER
[ 1 ] Gerar informações da turma.
[ 2 ] Exibir arquivos .TXT disponíveis.
[ 3 ] Analisar arquivo da turma.
[ 4 ] Atualizar base de dados.
[ 5 ] ENCERRAR APLICAÇÃO.""")
    acao = input('O que deseja fazer: ')
    while acao not in ['1', '2', '3', '4', '5']:
        print('[ERRO] Ação inválida.')
        acao = input('O que deseja fazer: ')

    # COMANDO GERAR BASE DE DADOS
    if acao == '1':
        nome = input("Informe o nome do arquivo a ser criado: ").strip()
        while nome == "":
            nome = input("Informe o nome do arquivo a ser criado: ").strip()
        qtd = input("Quantos alunos deseja criar? ")
        while not qtd.isnumeric():
            print("[ERRO] Valor informado não é um número válido.")
            qtd = input("Quantos alunos deseja criar? ")
        gerarturma(nome, int(qtd))

    # COMANDO EXIBIR ARQUIVOS .TXT
    elif acao == '2':
        arquivos_txt = localizartxt()
        if len(arquivos_txt):
            print("-=-" * 30)
            print(f"Lista de arquivos encontrados: ", end=" ")
            for x in range(len(arquivos_txt)):
                if x == len(arquivos_txt) - 1:
                    print(arquivos_txt[x])
                else:
                    print(arquivos_txt[x], end=" | ")
            print("-=-" * 30)
            print()
        else:
            print("-=-" * 30)
            print("Não foram encontrados arquivos .TXT")
            print("-=-" * 30)
            print()

    # COMANDO ANALISAR BASE DE DADOS
    elif acao == '3':
        arquivos_txt = localizartxt()
        arquivo_entrada = input("Informe o arquivo a ser analisado [com formato]: ").strip().lower()
        while arquivo_entrada not in arquivos_txt:
            print('[ERRO] Arquivo não localizado. Tente novamente.')
            print(f'Arquivos disponíveis: {arquivos_txt}')
            arquivo_entrada = input("Informe o arquivo a ser analisado [com formato]: ").strip().lower()
        print("""Formatos disponíveis:
[ 1 ] Formato [.txt]
[ 2 ] Formato [.html]""")
        formato = input('Informe o formato do arquivo que deverá ser criado: ').strip()
        while formato not in ['1', '2']:
            formato = input('Informe o formato do arquivo que deverá ser criado: ').strip()
        if formato == '1':
            formato = 'txt'
        elif formato == '2':
            formato = 'html'
        analisarturma(formato, arquivo_entrada)

    # COMANDO ALTERAR BASE DE DADOS
    elif acao == '4':
        arquivos_txt = localizartxt()
        arquivo_entrada = input("Informe o arquivo a ser alterado [com formato]: ").strip().lower()
        while arquivo_entrada not in arquivos_txt:
            print('[ERRO] Arquivo não localizado. Tente novamente.')
            print(f'Arquivos disponíveis: {arquivos_txt}')
            arquivo_entrada = input("Informe o arquivo a ser alterado [com formato]: ").strip().lower()
        aluno = input("Informe o nome do aluno que deseja alteração: ").strip()
        print("""Informe o atributo que que deverá ser alterado:
[ 1 ] Nome do aluno
[ 2 ] Nota 01
[ 3 ] Nota 02
[ 4 ] Qtd. de Faltas""")
        atributo = input().strip()
        while atributo not in ['1', '2', '3', '4']:
            print('[ERRO] Atributo inválido.')
            atributo = input().strip()
        if atributo == '1':
            atributo = 'nome'
        elif atributo == '2':
            atributo = 'n1'
        elif atributo == '3':
            atributo = 'n2'
        elif atributo == '4':
            atributo = 'faltas'
        alterarbasedados(arquivo_entrada, aluno, atributo)

    # COMANDO ENCERRAR APLICAÇÃO
    elif acao == '5':
        print('-=-'*30)
        print("Aplicação Encerrada")
        print('-=-' * 30)
        system("PAUSE")
        break
