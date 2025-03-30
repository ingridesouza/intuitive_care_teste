# Extração e Processamento do Rol de Procedimentos - Intuitive Care

Este projeto foi desenvolvido como parte da questão 2 do teste de transformação de dados da **Intuitive Care**. Ele tem como objetivo extrair e estruturar os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF fornecido no Anexo I.

---

## Funcionalidades implementadas

- **Leitura de PDF:** utiliza a biblioteca `tabula-py` para extrair tabelas do arquivo `Anexo_I.pdf`, presente na pasta `doc/`, entre as páginas 3 e 181.
- **Tratamento de dados:**
  - Concatena todas as tabelas extraídas em um único `DataFrame`
  - Renomeia as colunas conforme os campos do rol
  - Remove linhas duplicadas e cabeçalhos repetidos
  - Aplica `strip()` e substitui `\n` por espaço
  - Substitui as siglas OD, AMB, HCO, HSO, etc. pelas descrições completas
- **Exportação para CSV:** gera um arquivo chamado `rol_de_procedimentos.csv` com os dados tratados.
- **Compactação:** cria um `.zip` nomeado `Teste_ingride.zip` contendo o CSV final

---

## Como executar

1. Instale as dependências:
```bash
pip install pandas tabula-py
```

2. Certifique-se de que o Java está instalado e configure o caminho na linha:
```python
'java_path': r"C:\Program Files\Java\jdk-24"
```

3. Execute o script:
```bash
python app.py
```

O arquivo final `Teste_ingride.zip` será gerado automaticamente com o CSV estruturado.

---

## Estrutura esperada do projeto
```
2transformarDados/
├── doc/
│   └── Anexo_I.pdf
├── app.py
├── rol_de_procedimentos.csv  ➔ (gerado pelo script)
└── Teste_ingride.zip       ➔ (gerado pelo script)
```

---

## Observação
- A solução está preparada para ser executada localmente em ambiente com suporte a Java.
- Toda a lógica está encapsulada em uma classe `PDFProcessor`, facilitando manutenção e testes.

---

## Autora
Projeto desenvolvido por **Ingride Souza** para teste de nivelamento da vaga na **Intuitive Care**. 

