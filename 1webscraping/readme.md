# Web Scraping - Download dos Anexos da ANS

Este script realiza uma automação simples de web scraping para baixar os arquivos "Anexo I" e "Anexo II" da página oficial da ANS.

---

## O que o script faz:

- Acessa o site da ANS com os documentos do Rol de Procedimentos  
- Varre todos os links `<a>` da página e identifica aqueles que mencionam **“Anexo I”** ou **“Anexo II”** (ou “1” e “2”)
- Realiza o **download automático dos PDFs**
- Salva os arquivos em uma pasta `downloads_ans/`
- Compacta os dois PDFs em um único arquivo chamado `anexos.zip`

---

## Como usar:

1. Instale as dependências:
```bash
pip install requests beautifulsoup4
```

2. Execute o script:
```bash
python baixar_anexos.py
```

---

## Saída esperada:
```
downloads_ans/
├── Anexo_I.pdf
├── Anexo_II.pdf
└── anexos.zip
```

---

## Autora
Projeto desenvolvido por **Ingride Souza** para teste de nivelamento da vaga na **Intuitive Care**. 

