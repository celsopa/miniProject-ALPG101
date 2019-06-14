from random import random, randint

notasTurma = []
situacaoTurma = []


def analisarturma(novo_arquivo, formato, base_dados):
    """
    Analisa um arquivo com dados dos alunos de uma classe e retorna uma tabela com a situação de cada um.
    :param novo_arquivo: Nome do novo arquivo onde serão salvas as informações da turma.
    :param formato: Formato do arquivo que será criado.
    :param base_dados: Nome do arquivo com indicação do formato onde constam os dados que serão analisados.
    :return: Um arquivo formatado contendo a situação de cada aluno informado.
    """
    arquivo = base_dados
    # arquivo = open(base_dados)
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
            conteudo.append(f"""{nome:^30}|{n1:^10}|{n2:^10}|{faltas:^10}|{resultado[0]:^10}|{resultado[1]:^10}\n""")

    estaticaturma = estaticasdaturma()
    arquivo.close()
    novo_arquivo = novo_arquivo + "." + formato
    arquivo = open(novo_arquivo, "w", encoding="UTF-8")
    if formato == "html":
        htmlinicio(arquivo)
        arquivo.writelines(conteudo)
        htmlfim(arquivo)
        arquivo.write(f"""<p>Média da turma: {estaticaturma[0]}</br>
        Quantidade de Alunos acima da média: {estaticaturma[1]}</br>
        Quantidade de alunos aprovados: {estaticaturma[2]}</br>
        Quantidade de alunos reprovados: {estaticaturma[3]}</br>
        Quantidade de alunos em recuperação: {estaticaturma[4]}</br>
        Quantidade de alunos reprovados por falta: {estaticaturma[5]}</br></p>""")
    else:
        arquivo.write(f"""{'NOME':^30}|{'NOTA 1':^10}|{'NOTA 2':^10}|{'FALTAS':^10}|{'MÉDIA':^10}|{'SITUAÇÃO':^10}\n""")
        arquivo.writelines(conteudo)
        arquivo.write(f"""\nMédia da turma: {estaticaturma[0]}
        Quantidade de Alunos acima da média: {estaticaturma[1]}
        Quantidade de alunos aprovados: {estaticaturma[2]}
        Quantidade de alunos reprovados: {estaticaturma[3]}
        Quantidade de alunos em recuperação: {estaticaturma[4]}
        Quantidade de alunos reprovados por falta: {estaticaturma[5]}""")
    arquivo.close()
    print(f"Criado o arquivo {novo_arquivo}.")


def htmlinicio(arquivo):
    arquivo.write(f"""<!DOCTYPE html>
        <html lang="pt-br">
          <head>
            <title>Notas da Turma</title>
            <meta charset="utf-8">
          </head>
          <body>
            <table border="1">
            <tr>
            <th>NOME</th>
            <th>NOTA 01</th>
            <th>NOTA 02</th>
            <th>FALTAS</th>
            <th>MÉDIA</th>
            <th>SITUAÇÃO</th>
            </tr>""")


def htmlfim(arquivo):
    arquivo.write("""</table>
        </body>
        </html>""")


def situacaoaluno(nota1=0.0, nota2=0.0, faltas=0):
    media = round((nota1 + nota2)/2, 2)
    if media < 5:
        situacao = "Reprovado"
    elif faltas >= 10:
        situacao = "Reprovado por falta"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"
    return media, situacao


def estaticasdaturma():
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
    arquivo = open(nome + str(qtd) + "alunos.txt", 'w', encoding="UTF-8")
    for x in range(1, qtd+1):
        aluno = ("Aluno " + str(x)).title()
        n1 = round(random() * 10, 2)
        n2 = round(random() * 10, 2)
        faltas = randint(1, 15)
        arquivo.write(f"{aluno}|{n1}|{n2}|{faltas}\n")
    arquivo.close()
    print(f"Criado o arquivo {arquivo.name}")


# analisarturma("teste", 'html', 'base1.txt')
