-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

SELECT 
    o.razao_social,
    dados.reg_ans,
    SUM(CAST(REPLACE(dados.vl_saldo_final, ',', '.') AS DECIMAL(15,2))) AS total_despesa
FROM (
    SELECT reg_ans, vl_saldo_final, descricao FROM t_contas_1T2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM t_contas_2T2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM t_contas_3T2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM t_contas_4T2024
) AS dados
JOIN operadoras_cadop o ON o.registro_ans = dados.reg_ans
WHERE dados.descricao LIKE '%EVENTOS%'
  AND dados.descricao LIKE '%CONHECIDOS%'
  AND dados.descricao LIKE '%MEDICO%'
GROUP BY dados.reg_ans, o.razao_social
ORDER BY total_despesa DESC
LIMIT 10;
