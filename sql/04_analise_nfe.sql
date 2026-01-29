SELECT 
    n.chave_nfe,
    n.valor_total_nfe,
    SUM(np.valor_pagamento) AS total_registrado_pagamento,
    (SUM(np.valor_pagamento) - n.valor_total_nfe) AS diferenca
FROM nfe n
JOIN nfe_pagamento np ON n.chave_nfe = np.chave_nfe
GROUP BY n.chave_nfe, n.valor_total_nfe
HAVING SUM(np.valor_pagamento) > n.valor_total_nfe
ORDER BY diferenca DESC;