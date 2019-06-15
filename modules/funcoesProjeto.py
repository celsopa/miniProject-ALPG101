from random import random, randint
from os import listdir
import re


notasTurma = []
situacaoTurma = []


def localizartxt():
    """
    Procura no diretório raiz por arquivos no formato .TXT
    :return: [list] Uma lista contendo todos os arquivos no formato .TXT
    """
    items = listdir("./")
    arquivos_txt = []
    for item in items:
        if item.endswith(".txt") and not item.endswith("analisado.txt"):
            arquivos_txt.append(item)
    return arquivos_txt


def analisarturma(formato, base_dados):
    """
    Analisa um arquivo com dados dos alunos de uma classe e retorna uma tabela com a situação de cada um.
    Também alimenta as listas [notasTurma] e [situacaoTurma], usados pela função [estaticasdaturma].
    :param formato: Formato do arquivo que será criado.
    :param base_dados: Nome do arquivo com indicação do formato onde constam os dados que serão analisados.
    :return: Um arquivo formatado contendo a situação de cada aluno informado.
    """
    arquivo = open(base_dados, "r", encoding='UTF-8')
    conteudo = []
    for line in arquivo:
        linhas = line.split('|')
        nome = linhas[0].strip()
        n1 = float(linhas[1].strip())
        n2 = float(linhas[2].strip())
        faltas = int(linhas[3].strip())
        resultado = situacaoaluno(n1, n2, faltas)
        notasTurma.append(resultado[0])
        situacaoTurma.append(resultado[1])
        if formato == "html":
            conteudo.append(f"""<tr>
                        <td>{nome}</td><td>{n1}</td><td>{n2}</td><td>{faltas}</td><td>{resultado[0]}</td><td>{
            resultado[1]}</td>
                        </tr>""")
        else:
            conteudo.append(f"""{nome:^30}|{n1:^10}|{n2:^10}|{faltas:^10}|{resultado[0]:^10}|{resultado[1]:^20}\n""")

    estaticaturma = estaticasdaturma()
    arquivo.close()
    base_dados = base_dados.split('.')[0]
    novo_arquivo = base_dados + "_analisado" + "." + formato
    arquivo = open(novo_arquivo, "w", encoding="UTF-8")
    if formato == "html":
        htmlinicio(arquivo)
        arquivo.writelines(conteudo)
        arquivo.write(f"""</table>
        </div>
        <div id="resumo">
        <h3>Resumo da Turma</h3>
        <p>Média da turma: {estaticaturma[0]}</p>
        <p>Alunos acima da média: {estaticaturma[1]}</p>
        <p>Alunos aprovados: {estaticaturma[2]}</p>
        <p>Alunos reprovados: {estaticaturma[3]}</p>
        <p>Alunos em recuperação: {estaticaturma[4]}</p>
        <p>Alunos reprovados por falta: {estaticaturma[5]}</p>
        </div>
        </div>
        </body>
        </html>""")
    else:
        arquivo.write(f"""{'NOME':^30}|{'NOTA 1':^10}|{'NOTA 2':^10}|{'FALTAS':^10}|{'MÉDIA':^10}|{'SITUAÇÃO':^20}\n""")
        arquivo.writelines(conteudo)
        arquivo.write(f"""\n\n\t\tRESUMO DA TURMA
    Média da turma: {estaticaturma[0]}
    Aluno acima da média: {estaticaturma[1]}
    Alunos aprovados: {estaticaturma[2]}
    Alunos reprovados: {estaticaturma[3]}
    Alunos em recuperação: {estaticaturma[4]}
    Alunos reprovados por falta: {estaticaturma[5]}""")
    arquivo.close()
    print(f"Criado o arquivo [{novo_arquivo}]\n")


def htmlinicio(arquivo):
    """
    Escreve a estrutura html inicial ao arquivo informado.
    :param arquivo: Um arquivo já aberto.
    :return: [No return].
    """
    arquivo.write(f"""<!DOCTYPE html>
        <html lang="pt-br">
          <head>
            <title>Notas da Turma</title>
            <meta charset="utf-8">
            <style>
                body{{
                    width: auto;
                    height: auto;
                    background: #bee5f4;
                    display: flex;
                    flex-direction: row;
                    justify-content: center;
                    align-items: center;
                }}
                h1{{
                    font-size: 30pt;
                    text-align: center;
                }}
                #conteudo{{
                    background-color: #e9f6fb;
                    margin: 20px auto;
                    padding: 20px;
                    width: auto;
                    height: auto;
                    border-radius: 10px;
                }}
                #tabela{{
                    position: relative;
                    float:left;
                    width: auto;
                    text-aligne: center;
                    margin-right: 10px;
                }}
                #tabela th{{
                    font-size: 16pt;
                }}
                #tabela td{{
                    text-align: center;
                    padding: 2px 10px;
                }}
                #resumo{{
                    position: relative;
                    font-size: 14pt;
                    float:left;
                    width: auto;
                    margin-left: 10px;
                    padding: 10px;
                    border-radius: 10px;
                }}
                #resumo h3{{
                    text-align: center;
                }}
            </style>
          </head>
          <body>
            <div id="conteudo">
            <h1>Análise da Classe</h1>
            <div id="tabela">
                <table border="1">
                <tr>
                <th>NOME</th>
                <th>NOTA 01</th>
                <th>NOTA 02</th>
                <th>FALTAS</th>
                <th>MÉDIA</th>
                <th>SITUAÇÃO</th>
                </tr>""")


def situacaoaluno(nota1, nota2, faltas):
    """
    Recebe como parâmetro duas notas (números reais) e a quantidade de faltas (número inteiro).
    Analisa os valores recebidos e retorna a média do aluno e sua situação.
    :param nota1: Número real correspondente à nota 1 do aluno.
    :param nota2: Número real correspondente à nota 2 do aluno.
    :param faltas: Número inteiro correspondente à quantidade de faltas do aluno.
    :return: Um par formado pelas variáveis [media] e [situacao].
    """
    media = round((nota1 + nota2)/2, 2)
    if faltas >= 10:
        situacao = "Reprovado por falta"
    elif media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"
    return media, situacao


def estaticasdaturma():
    """
    Manipula as listas de escopo global [notasTurma] e [situacaoTurma].
    Analisa a situação geral da turma. Calculando a média geral, quantidade de alunos acima da média
    e a quantidade de alunos em cada situação.
    :return: 06 variáveis correspondentes a média da classe, quantidade de alunos acima da média,
    quantidade de alunos aprovados, reprovados, em recuperação e reprovados por falta.
    """
    media = round(sum(notasTurma) / len(notasTurma), 2)
    qtdacimamedia = 0
    for n in notasTurma:
        if n >= media:
            qtdacimamedia += 1
    qtdaprovados = situacaoTurma.count('Aprovado')
    qtdreprovados = situacaoTurma.count('Reprovado')
    qtdrecuperacao = situacaoTurma.count('Recuperação')
    qtdreprovfaltas = situacaoTurma.count('Reprovado por falta')
    return media, qtdacimamedia, qtdaprovados, qtdreprovados, qtdrecuperacao, qtdreprovfaltas


def gerarturma(nome, qtd=1):
    """
    Cria um arquivo [.TXT] que servirá de base de dados representando uma classe de aula.
    Contém uma quantidade definida de alunos com elementos atribuídos aleatoriamente.
    Ao final exibe o nome do arquivo criado.
    :param nome: [String] Nome do arquivo de texto a ser criado.
    :param qtd: [Número inteiro] Quantidade de alunos a serem criados.
    :return: [No return].
    """
    arquivo = open(nome + ".txt", 'w', encoding="UTF-8")
    for x in range(1, qtd+1):
        aluno = ("Aluno_" + str(x)).title()
        n1 = round(random() * 10, 2)
        n2 = round(random() * 10, 2)
        faltas = randint(1, 15)
        arquivo.write(f"{aluno}|{n1}|{n2}|{faltas}|\n")
    arquivo.close()
    print(f"Criado o arquivo {arquivo.name} com {qtd} alunos.\n")


def alterarbasedados(base_dados, aluno, dado):
    """
    Altera uma informação específica da base de dados informada.
    Recebe o arquivo .TXT contendo a base de dado, o nome do aluno e o respectivo atributo
    que se deseja alterar.
    Ao final, caso o banco de dados já tenha sido analisado é feita uma nova análise automática.
    :param base_dados: [string] Nome do arquivo contendo os dados da turma.
    :param aluno: [string] Nome do aluno cuja informação deve ser alterada.
    :param dado: [string] Informação a ser alterada.
    :return: [No return]
    """
    arquivo = open(base_dados, "r", encoding="UTF-8")
    conteudo = []
    achou = 0
    for linha in arquivo:
        buscaAluno = linha.split('|')[0]
        if buscaAluno.strip().lower() == aluno.strip().lower():
            achou = 1

            # ALTERA O NOME DO ALUNO
            if dado == "nome":
                dado = r"\b{}\b".format(linha.split('|')[0])
                dadoVelho = linha.split("|")[0]
                dadoNovo = input(f'Novo NOME de {linha.split("|")[0]}: ').strip().title()
                linha = re.sub(dado, str(dadoNovo), linha)
                print(f'Nome de {dadoVelho} alterada para {dadoNovo}')
                conteudo.append(linha)

            # ALTERA A NOTA 01
            elif dado == "n1":
                dado = r"\b{}\b".format(linha.split('|')[1])
                dadoVelho = linha.split('|')[1]
                while True:
                    try:
                        dadoNovo = float(input(f'Nova NOTA 01 de {linha.split("|")[0]}: ').strip())
                        break
                    except:
                        print("[ERRO] Formato inválido.")
                linha = re.sub(dado, str(dadoNovo), linha)
                print(f'Nota 01 do aluno {linha.split("|")[0]} alterada de {dadoVelho} para {dadoNovo}')
                conteudo.append(linha)

            # ALTERA A NOTA 02
            elif dado == "n2":
                dado = r"\b{}\b".format(linha.split('|')[2])
                dadoVelho = linha.split('|')[2]
                while True:
                    try:
                        dadoNovo = float(input(f'Nova NOTA 02 de {linha.split("|")[0]}: ').strip())
                        break
                    except:
                        print("[ERRO] Formato inválido.")
                linha = re.sub(dado, str(dadoNovo), linha)
                print(f'Nota 02 do aluno {linha.split("|")[0]} alterada de {dadoVelho} para {dadoNovo}')
                conteudo.append(linha)

            # ALTERA A QTD DE FALTAS
            elif dado == "faltas":
                dado = r"\b{}\b".format(linha.split('|')[3])
                dadoVelho = linha.split('|')[3]
                while True:
                    try:
                        dadoNovo = int(input(f'Nova quantidade de faltas de {linha.split("|")[0]}: ').strip())
                        break
                    except:
                        print("[ERRO] Formato inválido.")
                linha = re.sub(dado, str(dadoNovo), linha)
                print(f'Faltas do aluno {linha.split("|")[0]} alterada de {dadoVelho} para {dadoNovo}')
                conteudo.append(linha)
        else:
            conteudo.append(linha)
    arquivo.close()
    arquivo = open(base_dados, "w", encoding="UTF-8")
    arquivo.writelines(conteudo)
    arquivo.close()
    if achou == 0:
        print("Aluno não encontrado.\nBase de dados não atualizada.\n")
    else:
        print("Base de dados atualizada.\n")
    items = listdir("./")
    for item in items:
        if item.endswith("analisado.txt"):
            analisarturma('txt', base_dados)
        if item.endswith("analisado.html"):
            analisarturma('html', base_dados)
