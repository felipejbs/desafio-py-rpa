FROM python:3.12-slim

# Instala dependências do sistema necessárias para requests-html e lxml
RUN apt-get update && \
    apt-get install -y build-essential libxml2-dev libxslt1-dev libffi-dev python3-dev curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala o pipenv e as dependências do projeto
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Comando padrão para rodar o crawler
CMD ["pipenv", "run", "python", "main.py"]