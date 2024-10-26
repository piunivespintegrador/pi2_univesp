# Univesp PI 2
Código do projeto integrador 2 usando Django 5.1.2

Crie um ambiente virtual (venv) do python3 

```python3 -m venv /path/to/new/virtual/environment```

Faça o acesso do seu venv do python3

```source /path/to/new/virtual/environment/bin/activate```

Para mais detalhes acesse [venv](https://docs.python.org/pt-br/3/library/venv.html)

Instale o DJango versão 5.1.2

```python3 -m pip install django==5.1.2```

Entre na pasta do projeto 

```cd lava jato```

Execute as migrations do DJango com o seguinte comando

```python manage.py migrate```

Rode o projeto

```python manage.py runserver```

O DJango irá dar acesso a página pelo ip ```http://127.0.0.1:8000/```
