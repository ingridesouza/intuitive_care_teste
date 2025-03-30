/* 
Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
*/

SELECT 
    o.razao_social,
    c.reg_ans,
    CAST(REPLACE(c.vl_saldo_final, ',', '.') AS DECIMAL(15,2)) AS valor_despesa
FROM t_contas_4T2024 c
JOIN operadoras_cadop o ON o.registro_ans = c.reg_ans
WHERE c.descricao LIKE '%EVENTOS%'
  AND c.descricao LIKE '%CONHECIDOS%'
  AND c.descricao LIKE '%MEDICO%'
ORDER BY valor_despesa DESC
LIMIT 10;
