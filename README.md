# analise-salarial-rh-pandas
Automação de análise salarial e indicadores de RH utilizando Python e Pandas. O projeto processa dados de colaboradores para identificar riscos de sucessão, anomalias de turnover e disparidades regionais/educacionais, gerando um relatório final em Excel com gráficos integrados.

# Sistema de Análise e Inteligência Salarial (RH)
Este projeto automatiza a extração de insights estratégicos a partir de bases de dados de recursos humanos. Utilizando Python e a biblioteca Pandas, o script realiza análises estatísticas avançadas e identifica padrões críticos para a gestão de talentos.

O script processa os dados brutos e gera cinco visões principais:
- **Análise Principal:** Cálculo de Mediana e MAD (Median Absolute Deviation) por cargo e localidade.
- **Comparativo Regional:** Diferença percentual de salários entre Capital e Interior.
- **Risco de Sucessão:** Identificação de colaboradores seniores (idade > 50 e tempo de casa > 15 anos) para planejamento de retenção de conhecimento.
- **Alertas de Turnover:** Detecção de anomalias salariais (Veteranos com salário baixo ou Novatos com salário alto).
- **Gap Educacional:** Cruzamento de remuneração por nível de escolaridade e cargo.

O sistema exporta um arquivo `.xlsx` contendo:
1. Tabelas dinâmicas formatadas.
2. Gráficos de colunas automatizados comparando as medianas salariais.
3. Dashboards segmentados por abas para facilitar a tomada de decisão gerencial.


- **Pandas**: Manipulação e tratamento de dados.
- **Numpy**: Operações matemáticas.
- **XlsxWriter**: Geração de relatórios Excel customizados com gráficos nativos.
