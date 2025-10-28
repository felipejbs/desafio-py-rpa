from requests_html import HTMLSession, HTML
from datetime import datetime
import json


def get_book_data(book: HTML, session: HTMLSession) -> dict[str, str]:
    """
    Extrai os dados de um livro a partir do elemento HTML e retorna um dicionário com as informações.
    """
    title: str = book.find('h3 a', first=True).attrs['title']
    price: str = book.find('p.price_color', first=True).text
    availability: str = book.find('p.instock.availability', first=True).text.strip()

    # Monta a URL da página do livro
    relative_link: str = book.find('h3 a', first=True).attrs['href']
    book_url: str = (
        "https://books.toscrape.com/catalogue/"
        f"{relative_link.replace('../../../', '')}"
    )
    book_page = session.get(book_url)

    # Extrai o gênero do livro
    breadcrumb = book_page.html.find('ul.breadcrumb li a')
    genero: str = breadcrumb[2].text if len(breadcrumb) > 2 else "Desconhecido"

    # Extrai a avaliação em estrelas
    # O resultado será o número de estrelas por extenso em inglês (ex: 'Three', 'Four', etc.)
    avaliacao: str = book_page.html.find('p.star-rating', first=True).attrs['class'][1]

    # Extrai a descrição do livro
    descricao_elem = book_page.html.find('#product_description + p', first=True)
    descricao: str = descricao_elem.text if descricao_elem else ""

    # Extrai informações adicionais da tabela
    linhas_da_tabela = book_page.html.find('table.table.table-striped tr')
    info: dict[str, str] = {}
    for tr in linhas_da_tabela:
        chave = tr.find('th', first=True).text
        valor = tr.find('td', first=True).text
        info[chave] = valor
    upc: str = info.get("UPC", "")
    tipo_produto: str = info.get("Product Type", "")

    # Retorna os dados do livro em um dicionário
    return {
        'title': title,
        'price': price,
        'genre': genero,
        'availability': availability,
        'avaliation': avaliacao,
        'description': descricao,
        'upc': upc,
        'product_type': tipo_produto,
        'product_url': book_url,
        'extraction_datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def scrape_books(num_pages: int = 5) -> list[dict[str, str]]:
    """
    Percorre as páginas do site e extrai os dados de todos os livros encontrados.
    """
    session: HTMLSession = HTMLSession()
    books_data: list[dict[str, str]] = []

    for page in range(1, num_pages + 1):
        page_url: str = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = session.get(page_url)

        if response.status_code == 200:
            books = response.html.find('article.product_pod')
            for book in books:
                book_data = get_book_data(book, session)
                books_data.append(book_data)

    return books_data


def save_books_data(books_data: list[dict[str, str]], filename: str = "books_data.json") -> None:
    """
    Salva os dados dos livros em um arquivo JSON dentro da pasta 'data'.
    """
    filepath: str = f"data/{filename}"
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(books_data, file, ensure_ascii=False, indent=4)


def main() -> None:
    """
    Função principal: extrai os dados dos livros, imprime a quantidade e salva em arquivo.
    """
    books_data: list[dict[str, str]] = scrape_books(num_pages=5)
    print(len(books_data))
    save_books_data(books_data)


if __name__ == "__main__":
    main()