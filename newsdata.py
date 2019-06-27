#! python 3.7.3

import psycopg2


# Pergunta 1 Quais os 3 artigos mais populares de todos os tempos?
query_artigos = """select articles.title, count(*) as views
                    from articles inner join log on log.path
                    like concat('%', articles.slug, '%')
                    where log.status like '%200%' group by
                    articles.title, log.path order by views desc limit 3"""

# Pergunta 2 Quais os autores de artigos mais populares de todos os tempos?
query_autores = """select authors.name, count(*) as views from articles inner
                    join authors on articles.author = authors.id inner join log
                    on log.path like concat('%', articles.slug, '%') where
                    log.status like '%200%' group
                    by authors.name order by views desc"""

# Pergunta 3 Em qual dia apenas menos de 1 porcento
# das requisicoes produziram erros?
query_erros = """select * from (
                  select access.day,
                  round(cast((100*errors.hits)
                  as numeric) / cast(access.hits as numeric), 2)
                  as percent from
                  (select date(time)
                  as day, count(*) as hits from log group by day) as access
                  inner join
                  (select date(time) as day, count(*) as hits from log
                  where status like '%404%' group by day) as errors
                  on access.day = errors.day)
                  as total where percent >= 1.0;"""


# Query do banco de dados
def query_db(sql_request):
    connect = psycopg2.connect(database="news")
    cursor = connect.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    connect.close()
    return results

# Exportando o resultado dentro de um arquivo txt
report = open("resultados.txt", "w+")


# Exportando a query dos artigos
def maiores_artigos():
    maiores_artigos = query_db(query_artigos)

    report.write("\n 3 Artigos mais lidos \n")

    for title, num in maiores_artigos:

        report.write("\n  {} -- {} views".format(title, num))


# Exportanto a query sobre os autores
def maiores_autores():
    maiores_autores = query_db(query_autores)

    report.write("\n\n 3 Autores mais lidos \n")

    for name, num in maiores_autores:

        report.write("\n  {} -- {} views".format(name, num))


# Exportanto a query dos erros
def logs_erros():
    logs_erros = query_db(query_erros)

    report.write("\n\n Dias com mais de um porcento de bad requests \n")

    for day, percent in logs_erros:
        report.write("\n  {} -- {} % errors\n".format(day, percent))


if __name__ == '__main__':
    maiores_artigos()
    maiores_autores()
    logs_erros()
