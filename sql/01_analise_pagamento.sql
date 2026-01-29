SELECT 
    e.id_empenho,
    e.valor AS valor_empenhado,
    SUM(p.valor) AS total_pago,
    (SUM(p.valor) - e.valor) AS diferenca
FROM empenho e
JOIN pagamento p ON e.id_empenho = p.id_empenho
GROUP BY e.id_empenho, e.valor
HAVING SUM(p.valor) > e.valor
ORDER BY diferenca DESC;