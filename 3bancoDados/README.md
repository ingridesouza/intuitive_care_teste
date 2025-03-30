# Projeto SQL – Análise de Demonstrativos Contábeis das Operadoras da ANS

Este projeto foi desenvolvido como parte de um **teste de nivelamento técnico para a Intuitive Care**. O objetivo é estruturar um banco de dados em MySQL com base em dados públicos da ANS, permitindo realizar análises financeiras a partir das demonstrações contábeis e do cadastro das operadoras de planos de saúde.

---

## Estrutura de Pastas

```
3bancoDados/
├── Criando banco/
├── Criando as tabelas e importando dados/
├── docs/
├── Query Analítica - Ultimo ano/
├── Query Analítica - Ultimo trimestre/
└── README.md
```

### `Criando banco/`
Contém o script responsável pela criação do banco de dados `db_financeiro`, utilizado para armazenar todas as tabelas do projeto.

### `Criando as tabelas e importando dados/`
Inclui os scripts `.sql` com comandos `CREATE TABLE` e `LOAD DATA LOCAL INFILE` utilizados para estruturar e importar os dados dos trimestres de 2023 e 2024, além das informações cadastrais das operadoras ativas.

### `docs/`
Reúne todos os arquivos de dados utilizados no projeto, incluindo:
- Demonstrativos contábeis trimestrais (`1T2023.csv`, `4T2024.csv` etc.)
- Relatório cadastral das operadoras
- Dicionário de dados com as definições dos campos

### `Query Analítica - Ultimo trimestre/`
Contém uma consulta SQL que identifica as 10 operadoras com as maiores despesas na categoria:
> *"EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO-HOSPITALAR"*

Filtrando apenas o **último trimestre disponível (4T2024)**.

### `Query Analítica - Ultimo ano/`
Consulta consolidada que analisa a mesma categoria ao longo de **todo o ano de 2024**, somando os valores dos quatro trimestres e retornando as 10 operadoras com maior despesa total.

---

## Tecnologias utilizadas

- **MySQL 8+**
- Codificação dos arquivos: `UTF-8` (com tratamento de vírgulas em valores decimais via `REPLACE`)
- Fontes de dados:
  - https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
  - https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

---

## Ordem de execução sugerida

1. Execute o script de **criação do banco de dados**.
2. Em seguida, rode os scripts de **criação das tabelas** e **importação dos dados** (por trimestre e cadastro).
3. Por fim, execute as **queries analíticas**.

---

## Autora
Projeto desenvolvido por **Ingride Souza** para teste de nivelamento da vaga na **Intuitive Care**. 