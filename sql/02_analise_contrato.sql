SELECT 
    c.id_contrato,
    c.valor AS valor_teto_contrato,
    SUM(e.valor) AS total_empenhado,
    (SUM(e.valor) - c.valor) AS excesso
FROM contrato c
JOIN empenho e ON c.id_contrato = e.id_contrato
GROUP BY c.id_contrato, c.valor
HAVING SUM(e.valor) > c.valor
ORDER BY excesso DESC;