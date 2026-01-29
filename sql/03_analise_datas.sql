SELECT 
    p.id_pagamento,
    p.valor,
    p.datapagamentoempenho AS data_pagamento,
    e.data_empenho,
    (e.data_empenho - p.datapagamentoempenho) AS dias_de_antecedencia_invalida
FROM pagamento p
JOIN empenho e ON p.id_empenho = e.id_empenho
WHERE p.datapagamentoempenho < e.data_empenho
ORDER BY dias_de_antecedencia_invalida DESC;