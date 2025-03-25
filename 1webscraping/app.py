import requests
from bs4 import BeautifulSoup
import os
import zipfile
from urllib.parse import urljoin
import re

def main():
    """
    Esse script acessa a página da ANS onde constam diversos links para arquivos PDF,
    varre todas as tags <a> para identificar apenas aquelas na qual o texto menciona
    "Anexo I" ou "Anexo II" (ou "Anexo 1" e "Anexo 2"). Se encontrar,
    baixa esses dois arquivos e compacta em um único arquivo ZIP.
    """

    # URL da página
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    # Faz a requisição ao site
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Não foi possível acessar {base_url}. status: {response.status_code}")
        return

    # Faz o parsing do HTML
    soup = BeautifulSoup(response.text, "html.parser")

    links_encontrados = []
    for link in soup.find_all("a", href=True):
        texto_link = link.get_text(strip=True)
        href_link = link["href"]

        # Localiza links que terminem em .pdf
        if href_link.lower().endswith(".pdf"):
            links_encontrados.append((texto_link, href_link))

    if not links_encontrados:
        print("Nenhum link(PDF) foi encontrado na página.")
        return

    # Filtro por aqueles que mencionem Anexo I e Anexo II utilizando expressões regulares
    pdf_links = {}

    for texto, href in links_encontrados:
        texto_lower = texto.lower()


        if re.search(r'\banexo\s*ii\b', texto_lower) or re.search(r'\banexo\s*2\b', texto_lower):
            pdf_links["Anexo_II"] = urljoin(base_url, href)

        elif re.search(r'\banexo\s*i\b', texto_lower) or re.search(r'\banexo\s*1\b', texto_lower):
            pdf_links["Anexo_I"] = urljoin(base_url, href)

    if not pdf_links:
        print("Não foram encontrados links de Anexo I ou Anexo II entre os PDFs.")
        return


    download_dir = "downloads_ans"
    os.makedirs(download_dir, exist_ok=True)

    # Baixa os pdfs
    for anexo_chave, anexo_url in pdf_links.items():
        nome_arquivo = f"{anexo_chave}.pdf"
        caminho_arquivo = os.path.join(download_dir, nome_arquivo)

        print(f"Baixando {anexo_chave} de: {anexo_url}")
        resp = requests.get(anexo_url)
        if resp.status_code == 200:
            with open(caminho_arquivo, "wb") as f:
                f.write(resp.content)
            print(f"{nome_arquivo} baixado com sucesso em: {caminho_arquivo}")
        else:
            print(f"Falha ao baixar {nome_arquivo}. status: {resp.status_code}")

    # Compacta os arquivos em um ZIP
    zip_filename = "anexos.zip"
    zip_path = os.path.join(download_dir, zip_filename)

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for anexo_chave in pdf_links.keys():
            pdf_file = os.path.join(download_dir, f"{anexo_chave}.pdf")
            if os.path.exists(pdf_file):
                zipf.write(pdf_file, arcname=f"{anexo_chave}.pdf")

    print(f"\nDownload e compactação finalizados! Arquivo ZIP disponível em: {zip_path}")

if __name__ == "__main__":
    main()
