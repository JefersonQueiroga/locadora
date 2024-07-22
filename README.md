# Nome do Projeto

Projeto da disciplina de Programação para Internet - IFRN

## Sobre

Este projeto é uma aplicação web desenvolvida em Django, destinada a abordar e exercitar os conteúdos da disciplina de Programação para Internet, lecionada no 4º ano do curso Técnico em Informática. O objetivo principal é proporcionar aos alunos uma plataforma prática para aplicar conceitos teóricos aprendidos em sala de aula.

## Pré-requisitos

Liste os pré-requisitos necessários para rodar o projeto localmente.

- Python 3.x
- Django 3.x
- pip

## Instalação

Instruções passo a passo sobre como configurar o ambiente de desenvolvimento.

1. Clone o repositório:
    ```bash
    git clone https://github.com/JefersonQueiroga/locadora.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd locadora
    ```

3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

6. Crie o arquivo `.env` a partir do exemplo `.env.example`:
    ```bash
    cp .env.example .env
    ```

7. Execute as migrações:
    ```bash
    python manage.py migrate
    ```

8. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

Instruções sobre como utilizar o projeto depois de configurado.

Acesse o servidor de desenvolvimento em [http://localhost:8000](http://localhost:8000).
