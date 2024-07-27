# Sistema de Upload e Conversão de Arquivos XLS para CSV

Este projeto é um sistema web em Django que permite o upload de arquivos XLS e a conversão desses arquivos para o formato CSV.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- Pip (Python package installer)

## Instalação

1. Clone o repositório do GitHub:

    ```sh
    git clone https://github.com/seu-usuario/upload-arquivo.git
    cd upload-arquivo
    ```

2. Crie um ambiente virtual:

    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```sh
        venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências do projeto:

    ```sh
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o admin do Django:

    ```sh
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

8. Acesse o sistema no navegador em `http://127.0.0.1:8000`.

## Estrutura do Projeto

- `import_xls/`: Diretório do projeto Django
  - `settings.py`: Configurações do Django
  - `urls.py`: Configurações de URLs do projeto
  - `asgi.py`: Configurações ASGI
  - `wsgi.py`: Configurações WSGI
- `conversor/`: Diretório do aplicativo Django
  - `models.py`: Modelos do aplicativo
  - `views.py`: Views do aplicativo
  - `urls.py`: URLs do aplicativo
  - `apps.py`: Configuração do aplicativo
- `templates/conversor/upload.html`: Template HTML para o upload de arquivos
- `requirements.txt`: Arquivo com as dependências do projeto

## Funcionalidades

- Upload de arquivos XLS
- Conversão de arquivos XLS para CSV
- Download de arquivos CSV convertidos

## Contribuição

1. Faça um fork do projeto
2. Crie um branch para sua feature (`git checkout -b minha-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adicionar nova feature'`)
4. Faça push para o branch (`git push origin minha-feature`)
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
