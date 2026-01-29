SELECT 
    f.nome AS nome_fornecedor,
    COUNT(DISTINCT c.id_contrato) AS quantidade_contratos,
    SUM(e.valor) AS total_dinheiro_empenhado
FROM fornecedor f
JOIN contrato c ON f.id_fornecedor = c.id_fornecedor
JOIN empenho e ON c.id_contrato = e.id_contrato
GROUP BY f.nome
ORDER BY total_dinheiro_empenhado DESC
LIMIT 10;