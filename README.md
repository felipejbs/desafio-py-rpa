# 📚 Book Scraper – Crawler em Python com Requests-HTML

Um **crawler em Python** que coleta informações de livros do site [Books to Scrape](https://books.toscrape.com/) e salva os dados em formato **JSON**.  

---

## 🚀 Funcionalidades

- Extração automatizada de:
  - Título do livro  
  - Preço  
  - Disponibilidade  
  - Gênero  
  - Avaliação (estrelas)  
  - Descrição  
  - Informações técnicas (UPC, tipo de produto)  
  - URL do produto  
  - Data e hora da extração  

- Armazenamento dos dados em um arquivo JSON bem formatado (`indent=4`, `ensure_ascii=False`).
- Suporte a múltiplas páginas.

---

## 🧠 Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | Python 3.12 |
| Web Scraping | [`requests-html`](https://requests-html.kennethreitz.org/) |
| Ambiente virtual | [`pipenv`](https://pipenv.pypa.io/) |
| Empacotamento | Docker |
| Padrão de código | PEP8 |

---

## 📁 Estrutura de Pastas

```
.
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── main.py
├── data/
│   └── books_data.json   # (gerado após execução)
└── README.md
```

---

## ⚙️ Instalação e Execução (sem Docker)

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/felipejbs/desafio-py-rpa.git
cd desafio-py-rpa
```

### 2️⃣ Instalar o Pipenv
```bash
pip install pipenv
```

### 3️⃣ Instalar as dependências
```bash
pipenv install
```

### 4️⃣ Executar o projeto
```bash
pipenv run python main.py
```

### 5️⃣ Ver o resultado
Os dados extraídos serão salvos no arquivo:
```
data/books_data.json
```

---

# 🐳 Execução com Docker

## 1. Build da imagem
```
docker build -t py-rpa-crawler .
```

## 2. Execute o container
```
docker run -d py-rpa-crawler
```

## 🧩 Estrutura do Código

### `main.py`

O código é modular e dividido em funções:

| Função | Descrição |
|--------|------------|
| `get_book_data(book, session)` | Extrai os dados de um livro específico. |
| `scrape_books(num_pages=5)` | Percorre as páginas e coleta os livros. |
| `save_books_data(books_data, filename)` | Salva os dados coletados em JSON. |
| `main()` | Função principal que orquestra o processo. |

---

## 🧱 Exemplo de Saída (`data/books_data.json`)

```json
[
    {
        "title": "A Light in the Attic",
        "price": "£51.77",
        "genre": "Poetry",
        "availability": "In stock (22 available)",
        "avaliation": "Three",
        "description": "It's hard to imagine a world without A Light in the Attic...",
        "upc": "A897FE39",
        "product_type": "Books",
        "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "extraction_datetime": "2025-10-27 17:45:30"
    }
]
```

---

## ✨ Boas Práticas Adotadas

- Código conforme **PEP 8** (formatação, indentação e nomes descritivos).
- Tipagem estática com *type hints* (`list[dict[str, str]]`).
- Funções pequenas e coesas.
- `ensure_ascii=False` para preservar acentuação no JSON.

---

## 🧪 Testes Rápidos

Para testar diferentes números de páginas:
```python
books_data = scrape_books(num_pages=5)
```

---

# Escolhas Técnicas e Trade-offs

## Linguagem e Bibliotecas

- **Python 3.12**  
  Escolhido por sua sintaxe moderna, tipagem opcional e ampla comunidade.
- **requests-html**  
  Permite scraping fácil de páginas web, com parsing HTML e suporte a JavaScript simples.  
- **lxml**  
  Usado como backend para parsing HTML, é rápido e eficiente.

## Estrutura do Projeto

- **Script único (`main.py`)**  
  Mantém o projeto simples e fácil de entender, ideal para projetos pequenos.
  **Trade-off:** Para projetos maiores, uma estrutura modular seria mais adequada.
- **Pasta `data/`**  
  Centraliza a saída dos dados, facilitando organização e acesso.

## Gerenciamento de Dependências

- **Pipenv**  
  Facilita o gerenciamento de ambientes virtuais e dependências, garantindo reprodutibilidade.
  **Trade-off:** Pipenv pode ser mais lento que o uso direto de `pip` e `requirements.txt`, mas oferece melhor isolamento.

## Containerização

- **Docker**  
  Garante que o projeto rode de forma idêntica em qualquer ambiente, evitando problemas de dependências de sistema.


## Scraping

- **Percorre páginas por URL sequencial**  
  Simples e eficiente para sites com estrutura previsível.
  **Trade-off:** Se o site mudar a estrutura de URLs ou adicionar proteção anti-bot, o crawler pode quebrar facilmente.

## Robustez

- **Sem tratamento avançado de erros**  
  O código assume que todas as páginas e elementos existem conforme esperado.
  **Trade-off:** Para uso em produção ou scraping de sites menos estáveis, seria necessário adicionar mais validações e tratamento de exceções.

---

## Resumo

As escolhas priorizaram **simplicidade, clareza e facilidade de execução** para um projeto de pequeno porte e propósito de exemplo.  
Para projetos maiores, mais robustos ou colaborativos, seria recomendado modularizar o código, e adicionar tratamento de erros

## 🧰 Possíveis Melhorias Futuras

- Adicionar logs estruturados (`logging`).
- Armazenar os dados em banco SQL (SQLite ou PostgreSQL) ou NoSQL (DynamoDB, etc.).
- Implementar testes automatizados com `pytest`.

---

## 👨‍💻 Autor

**Felipe Jerônimo Bernardo da Silva**  
📧 [felipejeronimobs@gmail.com]
🚀 Projeto desenvolvido como desafio de RPA/Web Scraping com Python.
