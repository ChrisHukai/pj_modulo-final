      _________      ___    ___    __________     _____        _________
     /.....____|    |..|   |..|   |...___...|     |...|     /....._____|
    /...../         |..|___|..|   |../   \..|     |...|     |..../
    |..../          |.._____..|   |..\___/../     |...|      \__ .\
    |.../           |..|   |..|   |...__.../      |...|         \_..\
    \....\          |..|   |..|   |..|   \..\     |...|           |...\
     \.....\        |..|   |..|   |..|    \..\    |...|           |...|
      \.....\____   |..|   |..|   |..|     \..\   |...|      ____/..../
       \________|   |__|   |__|   |__|      \__\  |___|      |_______/



##################################
	Made by: Chris Hukai
	christian.hukai@gmail.com
	~~ nTec rules ~~
##################################


==========
Introdução
==========
	> Um problema severo do nTec é... CRUD. Afinal, o que é um CRUD? Procure no Google dur
		1- Alguns projetos da Poli Jr. eram necessário ser criados mais de 50 CRUDs
		2- É algo que qualquer analista já sabe fazer... Vale à pena gastar refazendo isso?
	> Este módulo cria automaticamente CRUDs para você! Não somente CRUDs, mas os arquivos de template junto são gerados
	> This is the future!!

	> Script cria automaticamente...
		- Models, forms, urls
		- templates para display


============
Requirements/Details
============
	> Detail - Django: Última versão utilizada: 1.11
	> Detail - Python: Última versão utilizada 3.6
	> Detail - Success Url not defined

	> urls - CONEXÃO COM O APP:
		- Arquivo urls.py do app CONECTADO com a urls geral
			(Lembrando que... as urls são puxadas de um arquivo geral)
	> settings.py do app instalado
			(em installed_apps)

	> vanila - VIRTUAL ENV:
		- Baixar o vanilla no seu venv
		- Não sabe...? Perguntar para o gerente...!




====
BUGS
====
	> INDENTAÇÃO:
		- As indentações estão feitas por ESPAÇO, e não tab

	> TAG CONTENT:
		- Tag oficial utilizada para contents e {% block content %} em _base.html (no arquivo base.html)

	> template base - TEMPLATE BASE:
		- Para o programa funcionar, é necessário uma template base
			- Se não tiver template base, é necessário instá-la antes...
		- NOME DOS BLOCOS!!
			{% block title %} - para a tag <title>
			{% block content %} - para o conteúdo geral das páginas


============
BUGS IDIOTAS
============
	> NOME DA CLASSE:
		- As classes precisam ser criadas sem espaço! 



=============
Passo a Passo
=============
	> Colocar a PASTA modulo_final na pasta do app que você quer criar o CRUD
		(a pasta INTEIRA)




	> Ir para CADA arquivo para checar se os imports estão no topo
		models.py
		forms.py
		urls.py
=====================
O que não precisa ter
=====================
