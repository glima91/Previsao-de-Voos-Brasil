# Predição de Anormalidades em Voos Utilizando a Previsão do Tempo dos Aeroportos do Brasil (2019)

Projeto de conclusão do curso Machine Learning Engineer Nanodegree que tem como
objetivo desenvolver um modelo de classificador capaz de prever a ocorrência de
cancelamentos ou atrasos nos voos a partir da previsão do tempo (dos aeroportos) e o
horário dos voos. Para treinar o classificador foram utilizados os registros de voos e
previsões do tempo de 10 aeroportos de grande importância no Brasil.



## Informações Importantes:

- O script "parser.py" é responsável por unir os registros de voo e as previsões do tempo dos 
aeroportos em um único arquivo.

- o script "visuals.py" é responsável por gerar os gráficos no Jupyter Notebook

- Foram utilizadas as bibliotecas sklearn, pandas,matplotib, numpy,scipy e seaborn

- A pasta "Processamento" contém os dados dos 10 aeroportos utilizados para criar o modelo de classificação.

- A pasta "Processamento_Val" contém os dados de 4 aeroportos, utilizador para avaliar o desempenho do modelo com novos dados.
