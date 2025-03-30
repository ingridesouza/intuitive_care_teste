# Testes de Nivelamento - Intuitive Care

Este repositório reúne a solução completa para o **Teste de Nivelamento v.250321** proposto pela **Intuitive Care**, com foco em Web Scraping, Transformação de Dados, Banco de Dados e API com interface web.

---

## 1. Web Scraping

- Linguagem: **Python**
- Acesso à [página oficial da ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Busca e download automático dos arquivos **Anexo I** e **Anexo II** em formato PDF
- Compactação final em `anexos.zip`
- Script: `baixar_anexos.py`

---

## 2. Transformação de Dados

- Leitura e extração de dados do arquivo `Anexo I.pdf` (páginas 3 a 181)
- Utilização da biblioteca **tabula-py** para ler tabelas diretamente do PDF
- Tratamento de dados com **pandas**:
  - Renomeia colunas
  - Remove duplicatas e ruídos
  - Substitui siglas como OD, AMB, HCO por suas descrições completas
- Gera o arquivo `rol_de_procedimentos.csv`
- Compacta em `Teste_ingride.zip`
- Script: `app.py`

---

## 3. Banco de Dados - MySQL

- Criação do banco de dados `db_financeiro`
- Scripts SQL para:
  - Criar tabelas para cada trimestre (1T2023 a 4T2024)
  - Importar dados via `LOAD DATA LOCAL INFILE`
  - Inserir e estruturar os dados das operadoras (CSV)
- Queries analíticas:
  - Top 10 operadoras com maiores despesas no último trimestre (4T2024)
  - Top 10 operadoras com maiores despesas no último ano (2024)

### Fontes de dados:
- [Demonstrações contábeis da ANS](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
- [Cadastro das Operadoras](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

---

## 4. API + Interface Web

- API criada com **FastAPI**
- Rota `/buscar?termo=...` que permite busca textual por nome ou razão social de operadoras
- Leitura do CSV de operadoras com pandas
- Interface Web simples criada com **Vue.js (via CDN)** para interação
- Testes e documentação com **Postman**
- Arquivo Postman incluso na pasta `postman/`

### Estrutura do projeto
```
projeto_vue_operadoras/
├── backend/
│   └── main.py
├── frontend/
│   └── index.html
├── postman/
│   └── busca_operadoras_collection.json
```

---

## Organização do Repositório
```
/
├── 1webScraping/              # Web scraping e compactação dos anexos
├── 2transformarDados/         # Processamento do Anexo I e geração do CSV zipado
├── 3bancoDados/               # Scripts SQL, imports e queries analíticas
├── projeto_vue_operadoras/    # API + Interface Vue.js + Postman
└── README.md                  # Este arquivo
```

---

## Autora
Projeto desenvolvido por **Ingride Souza**.

Com este teste, busquei entregar soluções organizadas, bem documentadas e com foco em boas práticas de código e estrutura de dados. :)

