
CREATE TABLE t_contas_4T2023 (
    id_conta INT AUTO_INCREMENT PRIMARY KEY,
    data_movimento DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(15, 2) DEFAULT 0,
    vl_saldo_final DECIMAL(15, 2) DEFAULT 0
);


-- 3.4. Elabore queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.

LOAD DATA LOCAL INFILE 'C:/Users/Ingride/Documents/intuitive_care_teste/3bancoDados/docs/4T2023.csv'
INTO TABLE t_contas_4T2023
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(data_movimento, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final   = REPLACE(@vl_saldo_final, ',', '.');
