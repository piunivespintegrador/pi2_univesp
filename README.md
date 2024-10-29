# Univesp PI 2
Código do projeto integrador 2 usando Django 5.1.2

Crie um ambiente virtual (venv) do python3 

```python3 -m venv /path/to/new/virtual/environment```

Faça o acesso do seu venv do python3

```source /path/to/new/virtual/environment/bin/activate```

Para mais detalhes acesse [venv](https://docs.python.org/pt-br/3/library/venv.html)

Instalação do DJango Versão 5.1.2

```python3 -m pip install django==5.1.2```

Instalação do driver mysqlclient

```pip install mysqlclient```

* OBS: Se existir algum problema com o uso do mysqlclient, utilize o django-mysql

Instalação do django-mysql

```pip install django-mysql```

Faça a instalação do MySQL

Crie o banco de dados do projeto

```
CREATE DATABASE lava_jato CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON meu_banco_django.* TO 'seu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

Isso criará um banco de dados chamado ```lava_jato``` com o usuário ```seu_usuario``` com a senha ```sua_senha```

Entre na pasta do projeto 

```cd lava jato```

No arquivo python ```settings.py```, configure o DATABASES adicionado a senha e o usuário criado por você na criação do banco de dados.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lava_jato',     # Nome do banco de dados
        'USER': 'seu_usuario',   # Usuário do banco de dados
        'PASSWORD': 'sua_senha', # Senha do banco de dados
        'HOST': 'localhost',     # Endereço do servidor (pode ser 'localhost' para local)
        'PORT': '3306',          # Porta do MySQL, geralmente 3306
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

Verifique a conexão com o banco de dados

```python manage.py check```

Execute as migrations do DJango

```python manage.py migrate```

Rode o Faker Data para popular o banco com dados para testes (Use apenas para testes)

```python manage.py populate_data```

Rode o projeto

```python manage.py runserver```

O DJango irá dar acesso a página pelo ip ```http://127.0.0.1:8000/```
