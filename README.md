# Univesp PI 2

Projeto Integrador II

## Link Demo:

### Página pública

* [Página do Cliente](https://pi2-univesp.onrender.com/)

### Página administração

* [Página da Administração](https://pi2-univesp.onrender.com/admin)

```
OBS: A página de administração não esta protegido pois é apenas um trabalho para o projeto integrador e não algo comercial.
```

# UML - Entidade Relacionamento do MySQL e do MongoDB

<img src="UML/Vers%C3%A3o_1.4_UML_DB.png">

```
OBS: A edição do site (UML do MongoDB) não foi desenvolvido, assim como o sistema de edição dos dados da consulta
```

## Participantes:

```
Angra Dias de Olivera
Bruno Rosendo Alves
Felipe de Oliveira
Gabriel Antonio Ribeiro da Silva
Lucas Campos Achcar
Lucas Edson Santos Silva
Raquel Alves Nogueira Santos
Silvio Soares Pereira
```

## Instalação e Configuração

Código do projeto integrador 2 usando Django 5.1.2 e Python 3.12.3

Crie um ambiente virtual (venv) do python3 

```
python3 -m venv /path/to/new/virtual/environment
```

Faça o acesso do seu venv do python3

```
source /path/to/new/virtual/environment/bin/activate
```

Para mais detalhes acesse [venv](https://docs.python.org/pt-br/3/library/venv.html)

Instalação das Dependências do Projeto

```
pip install -r requirements.txt
```

Faça a instalação do MySQL (Docker)

Crie o banco de dados do projeto

```
CREATE DATABASE lava_jato CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON meu_banco_django.* TO 'seu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

Isso criará um banco de dados chamado ```lava_jato``` com o usuário ```seu_usuario``` com a senha ```sua_senha```

Entre na pasta do projeto 

```
cd lava jato
```

Faça uma copia do arquivo ```.env-exemplo``` e crie um arquivo  ```.env``` na mesma pasta, abra o arquivo e edite as credenciais do MySQL

```
DB_NAME=lava_jato       # nome do banco de dados
DB_USER=seu_usuario     # usuário do banco de dados
DB_PASSWORD=sua_senha   # senha do banco de dados
DB_HOST=127.0.0.1       # ou o IP do servidor de banco de dados
DB_PORT=3306            # porta padrão do MySQL
}
```

Verifique a conexão com o banco de dados

```
python manage.py check
```

Crie os arquivos das migrations

```
python manage.py makemigrations
```

Execute as migrations no bancos

```
python manage.py migrate admin --database=default
python manage.py migrate auth --database=default
python manage.py migrate sessions --database=default

python manage.py migrate private_site --database=mysql_db
python manage.py migrate public_site --database=mysql_db

python manage.py migrate private_site --database=mongo_db
python manage.py migrate public_site --database=mongo_db
```

Rode o Faker Data para popular o banco com dados para testes (Use apenas para testes)

```
python manage.py populate_data
```

Rode o projeto

```
python manage.py runserver
```

O DJango irá dar acesso a página pelo ip ```http://127.0.0.1:8000/```
