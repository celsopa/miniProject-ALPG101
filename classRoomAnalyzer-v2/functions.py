import os
import re
from random import random, randint
import webbrowser


class Aluno:
    def __init__(self, nome, n1, n2, faltas):
        self.nome = str(nome).strip().title()
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.faltas = int(faltas)


# Verifica se o diretório "./database" existe, caso contrário, cria esse diretório.
def checkdatabasedir():
    """
    Verify if the folder 'database' exists. If not, it is created.
    :return: [NO RETURN]
    """
    try:
        os.listdir("./database")
    except FileNotFoundError:
        os.makedirs("./database")


# Verifica se o diretório "./analises" existe, caso contrário, cria esse diretório.
def checkanalisesdir():
    """
    Verify if the folder 'analises' exists. If not, it is created.
    :return: [NO RETURN]
    """
    try:
        os.listdir("./analises")
    except FileNotFoundError:
        os.makedirs("./analises")


# Verifica se o número informado pode ser convertido para ponto flutuante
def isfloat(n):
    """
    Verify if the parameter can be converted to a float number.
    :param n: [string] A string to be verified.
    :return: [boolean] Returns 'true' if the string can be converted to float, otherwise returns 'falses'.
    """
    try:
        float(n)
        return True
    except ValueError:
        return False


# Retorna um dicionário com os arquivos da pasta 'database'
def listardb():
    """
    Creates a dictionary containing the files in the 'database' folder.
    Must be used in conjunction with the 'exibirdb' function. The keys are integers beginning with 1.
    :return: [dictionary] A dictionary with files in 'database' folder.
    """
    arquivosdb = {}
    checkdatabasedir()
    files = os.listdir("./database")
    for f in range(len(files)):
        arquivosdb[f+1] = files[f]
    return arquivosdb


# Exibe os arquivos database contidos na pasta
def exibirdb():
    """
    Prints the files in the 'database' folder with their respective keys.
    If a file is found, the user can choose which file to open.
    :return: [NO RETURN]
    """
    arquivosdb = listardb()
    print("=" * 40)
    if len(arquivosdb) == 0:
        print(f"{'NENHUM ARQUIVO DATABASE DISPONÍVEL':^40}")
    elif len(arquivosdb) == 1:
        print(f"{'ARQUIVO DATABASE DISPONÍVEL:':^40}")
        for k, v in arquivosdb.items():
            print(f"{k} -> {v}")
    else:
        print(f"{'ARQUIVOS DATABASE DISPONÍVEIS':^40}")
        for k, v in arquivosdb.items():
            print(f"{k} \u2192 {v}")
    print("=" * 40)



# Gerar um arquivo database com dados aleatórios
def turmaaleatoria():
    """
    Creates a new database file. The user enter the file name and how many students to create.
    The students datas are created randomly:
    i) name - string,
    ii) score 1 - float number, with two decimals points,
    iii) score 1 - float number, with two decimals points,
    iv) number os absenses - interger number, between 0 and 13.
    At the end, the created database file is analyzed.
    :return: [NO RETURN]
    """
    checkdatabasedir()
    nome = input("Informe o nome do arquivo database a ser criado: ").strip().lower()
    qtd = input("Informe a quantidade de alunos: ").strip()
    while not qtd.isnumeric():
        print("[ERRO] Informe um valor número válido")
        qtd = input("Informe a quantidade de alunos: ").strip()
    nomedb = nome
    arquivo = open("./database/" + nomedb, 'w', encoding="UTF-8")
    for x in range(1, int(qtd) + 1):
        aluno = Aluno(("Aluno_" + str(x)).title(), round(random() * 10, 2), round(random() * 10, 2), randint(0, 13))
        arquivo.write(f"{aluno.nome}|{aluno.n1}|{aluno.n2}|{aluno.faltas}|\n")
    arquivo.close()
    print(f"Criado o arquivo database [{nomedb}] com {qtd} alunos.")
    analisar(nomedb)


# Insere um novo aluno personalizado em uma database escolhida
def criaraluno():
    """
    Creates a student record. Firs, the user choose create or update a database file.
    After that, the user informs the name, score 1, score 2 and number of absences.
    At the end, the database file (created or updated) is analyzed.
    :return: [NO RETURN]
    """
    print("=" * 40)
    resp = input("CRIAR NOVA DATA BASE? [S/N]: ").strip().lower()[0]
    while resp not in 'sn':
        resp = input("CRIAR NOVA DATA BASE? [S/N]: ").strip().lower()[0]
    if resp == "s":
        db = input("Nome da nova database: ").strip().lower()
    else:
        print("=" * 40)
        exibirdb()
        listasdb = listardb()
        db = input("Informe a database que deseja alterar: ")
        while (not db.isnumeric()) or (int(db) <= 0) or (int(db) > len(listasdb)):
            print("[ERRO] ENTRADA INVÁLIDA.")
            db = input("Informe a database que deseja alterar: ")
        db = int(db)
        db = listasdb[db]
    print("=" * 40)
    print(f"{'CRIANDO NOVO ALUNO':^40}")
    print("=" * 40)
    arqdb = open("./database/" + db, "a", encoding="UTF-8")
    nome = input("Nome: ").strip().title()
    n1 = input("Nota 01: ").strip()
    while not isfloat(n1):
        print("[ERRO] VALOR INVÁLIDO.")
        n1 = input("Nota 01: ").strip()
    n2 = input("Nota 02: ").strip()
    while not isfloat(n2):
        print("[ERRO] VALOR INVÁLIDO.")
        n2 = input("Nota 02: ").strip()
    faltas = input("Faltas: ").strip()
    while not faltas.isnumeric():
        print("[ERRO] VALOR INVÁLIDO.")
        faltas = input("Faltas: ").strip()
    nome = Aluno(nome, n1, n2, faltas)
    arqdb.write(f"{nome.nome}|{nome.n1}|{nome.n2}|{nome.faltas}|\n")
    arqdb.close()
    print(f"Criado o aluno [{nome.nome}] no arquivo [{db}].")
    analisar(db)


# Altera os dados de um aluno específico da database escolhida
def alterarbasedados():
    """
    Updates a database file. The user can chose which file want to change.
    After, informs the name of student and the data to change.
    If the student is not found at database, it is printed on screen.
    Other wise, is printed the changes made and the updated database is analyzed.
    :return: [NO RETURN]
    """
    exibirdb()
    listasdb = listardb()
    if len(listasdb) != 0:
        db = input("Informe a database que deseja alterar: ")
        while (not db.isnumeric()) or (int(db) <= 0) or (int(db) > len(listasdb)):
            print("[ERRO] ENTRADA INVÁLIDA.")
            db = input("Informe a database que deseja alterar: ")
        db = int(db)
        db = listasdb[db]
        print("=" * 40)
        print(f"{'ALTERANDO DATABASE':^40}")
        print("=" * 40)
        arquivo = open("./database/" + db, "r", encoding="UTF-8")
        aluno = input("Informe o nome do aluno que deseja editar: ").strip()
        print(f"""Informe o dado que deseja alterar:
    [ 1 ] Nome
    [ 2 ] Nota 01
    [ 3 ] Nome 02
    [ 4 ] Faltas""")
        dado = input("Informe o dado que deseja alterar: ")
        while dado not in ["1", "2", "3", "4"]:
            print("[ERRO] ENTRADA INVÁLIDA")
            dado = input("Informe o dado que deseja alterar: ")
        if dado == "1":
            dado = 'nome'
        elif dado == "2":
            dado = 'n1'
        elif dado == "3":
            dado = 'n2'
        elif dado == "4":
            dado = 'faltas'
        conteudo = []
        achou = 0
        for linha in arquivo:
            buscaaluno = linha.split('|')[0]
            if buscaaluno.strip().lower() == aluno.strip().lower():
                achou = 1

                # ALTERA O NOME DO ALUNO
                if dado == "nome":
                    dado = r"\b{}\b".format(linha.split('|')[0])
                    dadovelho = linha.split("|")[0]
                    dadonovo = input(f'Novo NOME de {linha.split("|")[0]}: ').strip().title()
                    linha = re.sub(dado, str(dadonovo), linha)
                    print(f'Nome de [{dadovelho}] alterada para [{dadonovo}]')
                    conteudo.append(linha)

                # ALTERA A NOTA 01
                elif dado == "n1":
                    dado = r"\b{}\b".format(linha.split('|')[1])
                    dadovelho = linha.split('|')[1]
                    while True:
                        try:
                            dadonovo = float(input(f'Nova NOTA 01 de {linha.split("|")[0]}: ').strip())
                            break
                        except ValueError:
                            print("[ERRO] ENTRADA INVÁLIDA.")
                    linha = re.sub(dado, str(dadonovo), linha)
                    print(f'Nota 01 do aluno [{linha.split("|")[0]}] alterada de [{dadovelho}] para [{dadonovo}]')
                    conteudo.append(linha)

                # ALTERA A NOTA 02
                elif dado == "n2":
                    dado = r"\b{}\b".format(linha.split('|')[2])
                    dadovelho = linha.split('|')[2]
                    while True:
                        try:
                            dadonovo = float(input(f'Nova NOTA 02 de {linha.split("|")[0]}: ').strip())
                            break
                        except ValueError:
                            print("[ERRO] ENTRADA INVÁLIDA.")
                    linha = re.sub(dado, str(dadonovo), linha)
                    print(f'Nota 02 do aluno [{linha.split("|")[0]}] alterada de [{dadovelho}] para [{dadonovo}]')
                    conteudo.append(linha)

                # ALTERA A QTD DE FALTAS
                elif dado == "faltas":
                    dado = r"\b{}\b".format(linha.split('|')[3])
                    dadovelho = linha.split('|')[3]
                    while True:
                        try:
                            dadonovo = int(input(f'Nova quantidade de faltas de {linha.split("|")[0]}: ').strip())
                            break
                        except ValueError:
                            print("[ERRO] ENTRADA INVÁLIDA.")
                    linha = re.sub(dado, str(dadonovo), linha)
                    print(f'Faltas do aluno [{linha.split("|")[0]}] alterada de [{dadovelho}] para [{dadonovo}]')
                    conteudo.append(linha)
            else:
                conteudo.append(linha)
        arquivo.close()
        arquivo = open("./database/" + db, "w", encoding="UTF-8")
        arquivo.writelines(conteudo)
        arquivo.close()
        if achou == 0:
            print("Aluno não encontrado.\nBase de dados não atualizada.")
        else:
            print("Base de dados atualizada.")
        analisar(db)


# Analisa uma base de dados e gera um arquivo html contendo as informações de cada aluno e estatísticas gerais da turma
def analisar(db):
    """
    Analyzes a database file, creating an html file with the analyzed data.
    Invokes the 'htmlinicio' function to print the beginning of the file.
    :param db: [string] A string with the nome of database file.
    :return: [NO RETURN]
    """
    notasturma = []
    situacaoturma = []
    checkanalisesdir()
    arquivo = open("./database/" + db, "r", encoding="UTF-8")
    conteudo = []
    for line in arquivo:
        if line != "\n":
            linhas = line.split('|')
            nome = linhas[0].strip()
            n1 = float(linhas[1].strip())
            n2 = float(linhas[2].strip())
            faltas = int(linhas[3].strip())
            resultado = situacaoaluno(n1, n2, faltas)
            notasturma.append(resultado[0])
            situacaoturma.append(resultado[1])
            conteudo.append(f"""<tr>
                <td>{nome}</td>
                <td>{n1}</td>
                <td>{n2}</td>
                <td>{faltas}</td>
                <td>{resultado[0]}</td>
                <td>{resultado[1]}</td>
            </tr>""")
    estaticaturma = estaticasdaturma(notasturma, situacaoturma)
    arquivo.close()
    arquivo = open("./analises/" + db + ".html", "w", encoding="UTF-8")
    htmlinicio(arquivo)
    arquivo.writelines(conteudo)
    arquivo.write(f"""
        </table>
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
<script>
    linha = document.getElementsByTagName('tr');
    for (let x = 1; x < linha.length; x++){{
        if (linha[x].innerHTML.indexOf('<td>Aprovado</td>') === -1){{
            linha[x].style.backgroundColor = '#ff6666';
        }}
        if (linha[x].innerHTML.indexOf('<td>Recuperação</td>') !== -1){{
            linha[x].style.backgroundColor = '#ffe6e6';
        }}
        if (linha[x].innerHTML.indexOf('<td>Aprovado</td>') !== -1){{
            linha[x].style.backgroundColor = 'rgba(0, 4, 255, 0.2)';
        }}
    }}
</script>
</body>
</html>""")
    arquivo.close()
    print(f"Database [{db}] analisada.\n")


# Cabeçalho do arquivo html
def htmlinicio(arquivo):
    """
    Print the beginning of the html text of each analysis file.
    :param arquivo: [object] A file object created in writing mode.
    :return: [NO RETURN]
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
                    background-color: lightblue;
                    display: flex;
                    flex-direction: row;
                    justify-content: center;
                    align-items: center;
                }}
                table, td, th{{
                    border: 1px solid black;
                }}
                h1{{
                    font-size: 30pt;
                    text-align: center;
                }}
                #conteudo{{
                    background-color: rgba(0, 4, 255, 0.15);
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
                    text-align: center;
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
                <table>
                <tr>
                    <th>NOME</th>
                    <th>NOTA 01</th>
                    <th>NOTA 02</th>
                    <th>FALTAS</th>
                    <th>MÉDIA</th>
                    <th>SITUAÇÃO</th>
                </tr>""")


# Examina a situação de um aluno com base em duas notas e quantidade de faltas
def situacaoaluno(nota1, nota2, faltas):
    """
    Analyzes the situation of each student based on the score 1, score 2 and number of absences.
    i) More than 10 absences the student is automatically disapproved, regardless of his grades.
    ii) Average below 5 - disapproved.
    iIi) Average between 5 and 7 - in recovery.
    iv) Average above 7 - approved.
    :param nota1: [float] A float number representing the score 1.
    :param nota2: [float] A float number representing the score 2.
    :param faltas: [interger] [float] A interger number representing the number of absences.
    :return: [tuple] A tuple with the average and student situation.
    """
    media = round((nota1 + nota2) / 2, 2)
    if faltas >= 10:
        situacao = "Reprovado por falta"
    elif media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"
    return media, situacao


# Analisa as estatísticas da turma
def estaticasdaturma(notasturma, situacaoturma):
    """
    Calculate class statistics by providing the average class score, number of students above average,
    and number of students in each situation (approved, recovered, failed, failed due to absence).
    :param notasturma: [array] A array of each student's score.
    :param situacaoturma: [array] A array of each student's situation.
    :return: [tuple] A tuple with average class score, number of students above average,
    number of students approved, number of students recovered, number of students failed,
    number of students failed due to absence.
    """
    media = round(sum(notasturma) / len(notasturma), 2)
    qtdacimamedia = 0
    for n in notasturma:
        if n >= media:
            qtdacimamedia += 1
    qtdaprovados = situacaoturma.count('Aprovado')
    qtdreprovados = situacaoturma.count('Reprovado')
    qtdrecuperacao = situacaoturma.count('Recuperação')
    qtdreprovfaltas = situacaoturma.count('Reprovado por falta')
    return media, qtdacimamedia, qtdaprovados, qtdreprovados, qtdrecuperacao, qtdreprovfaltas


def listaranalise():
    """
    Creates a dictionary containing the files in the 'analises' folder.
    Must be used in conjunction with the 'exibiranalises' function. The keys are integers beginning with 1.
    :return: [dictionary] A dictionary with files in 'analises' folder.
    """
    arquivosanalise = {}
    checkanalisesdir()
    files = os.listdir("./analises")
    for f in range(len(files)):
        arquivosanalise[f+1] = files[f]
    return arquivosanalise


# Exibe os arquivos database contidos na pasta
def exibiranalises():
    """
    Prints the files in the 'analises' folder with their respective keys.
    If a file is found, the user can choose which file to open.
    :return: [NO RETURN]
    """
    arquivosanalise = listaranalise()
    print("=" * 40)
    if len(arquivosanalise) == 0:
        print(f"{'NENHUM ARQUIVO ANÁLISE DISPONÍVEL':^40}")
    elif len(arquivosanalise) == 1:
        print(f"{'ARQUIVO ANÁLISE DISPONÍVEL:':^40}")
        for k, v in arquivosanalise.items():
            print(f"{k} -> {v}")
    else:
        print(f"{'ARQUIVOS ANÁLISE DISPONÍVEIS':^40}")
        for k, v in arquivosanalise.items():
            print(f"{k} -> {v}")
    print("=" * 40)
    if len(arquivosanalise) != 0:
        arq = input("Selecione o arquivo a ser exibido: ").strip()
        while not arq.isnumeric():
            arq = input("Selecione o arquivo a ser exibido: ").strip()
        arquivo = "./analises/" + arquivosanalise[int(arq)]
        webbrowser.open(os.path.abspath(arquivo))
