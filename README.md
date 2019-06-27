# Análise de Logs

Terceiro projeto para meu Nanodegree de Desenvolvedor Web Full Stack.

## Qual é o projeto?

- Construir resultados informativos de logs a partir de um banco de dados real. Analizar milhares de linhas de dados em um banco e poder responder 3 perguntas.

 1. Quais são os três artigos mais populares de todos os tempos?
 2. Quem são os autores de artigos mais populares de todos os tempos?
 3. Em quais dias mais de 1% das requisições resultaram em erros?


## Pré-requisitos para executar o programa.
  - Python 3
  - A biblioteca de conexão com Python Psycopg2
  - A máquina vitual com as configurações cedidas pela Udacity , link na seção Modo de uso.
  - O Banco de dados newsdata.sql também com link na seção Modo de uso.


## Desenvolvimento

Esse projeto usa Python em conjunto com a DB-API.
Ambos os códigos Python e SQL seguem suas referências de boas práticas.
Todas as querys e códigos rodam dentro de uma máquina virtual Linux configurada usando Vagrant e cedida pela própria Udacity.

## Modo de uso.

 - Você precisará baixa e instalar o [Vagrant](https://www.vagrantup.com/).
 - E também a versão mais recente do [Virtual Box](https://www.virtualbox.org/).
 - Clone a [Máquina Virtual da Udacity](https://github.com/udacity/fullstack-nanodegree-vm).
 - Baixe [aqui](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). o arquivo newsdata.sql. Extraia dentro do da pasta compartilhada com a MV.
  - Para começar trabalhando no arquivo apenas use os comandos a seguir dentro da página onde sua MV está instalada:
    - ```vagrant up``` Inicia a máquina virtual.
    - ```vagrant ssh``` da o acesso a máquina virtual.
    - ```cd /vagrant``` Caminha até o diretório compartilhado.
    - ```psql -d news -f newsdata.sql``` Carrega os dados do arquivo e cria todas as tabelas necessárias.
    - ```python newsdata.py``` Finalmente rode o arquivo e receba os resultados através do arquivo "resultados.txt"