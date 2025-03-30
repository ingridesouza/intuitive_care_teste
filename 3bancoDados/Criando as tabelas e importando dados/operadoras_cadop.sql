CREATE TABLE operadoras_cadop (
    id_operadora INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT NOT NULL,
    cnpj BIGINT NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100) NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    complemento VARCHAR(100),
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL,
    cep INT NOT NULL,
    ddd INT,
    telefone BIGINT,
    fax BIGINT,
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255) NOT NULL,
    cargo_representante VARCHAR(100) NOT NULL,
    regiao_de_comercializacao INT,
    data_registro_ans DATE NOT NULL
);



-- 3.4. Elabore queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.

LOAD DATA LOCAL INFILE 'C:/Users/Ingride/Documents/intuitive_care_teste/3bancoDados/docs/Relatorio_cadop.csv'
INTO TABLE operadoras_cadop
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
 logradouro, numero, complemento, bairro, cidade, uf, cep,
 @ddd, @telefone, @fax,
 endereco_eletronico, representante, cargo_representante, @regiao, @data_ans)
SET
    ddd = NULLIF(@ddd, ''),
    telefone = NULLIF(@telefone, ''),
    fax = NULLIF(@fax, ''),
    regiao_de_comercializacao = NULLIF(@regiao, ''),
    data_registro_ans = STR_TO_DATE(@data_ans, '%Y-%m-%d');

