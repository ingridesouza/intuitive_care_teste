# API de Busca de Operadoras - Intuitive Care

O objetivo é disponibilizar uma API simples e uma interface web para realizar buscas em um arquivo CSV contendo os dados das operadoras de planos de saúde cadastradas na ANS.

---

## Tecnologias utilizadas
- **Python**
- **FastAPI** para a construção da API
- **Pandas** para leitura e tratamento dos dados
- **Vue.js (via CDN)**
- **Postman** para testar e documentar a API

---

## Funcionalidades
- Leitura do arquivo `Relatorio_cadop.csv` com os dados das operadoras.
- Rota `/buscar` que permite realizar buscas textuais (GET) nas colunas `razao_social` e `nome_fantasia`.
- Tratamento de valores ausentes (`NaN`) para evitar erros na resposta JSON.
- Interface web simples feita com Vue.js para consultar os dados diretamente do navegador.

---

## Como executar

1. Instale as dependências com:
```bash
pip install fastapi uvicorn pandas
```

2. Execute o servidor:
```bash
uvicorn backend.main:app --reload
```

3. Acesse a interface web abrindo o arquivo `frontend/index.html` em um navegador.

4. A rota da API também pode ser testada diretamente em:
```
http://localhost:8000/buscar?termo=amil
```

5. O teste da API também está documentado via **Postman** na pasta `/postman`, com o arquivo:
```
busca_operadoras_collection.json
```

---

## Estrutura do projeto

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

## Autora
Projeto desenvolvido por **Ingride Souza** para teste de nivelamento da vaga na **Intuitive Care**. 

