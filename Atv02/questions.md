### Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

- Para identificar outliers com o desvio padrão, primeiro calculamos a média e o desvio padrão da coluna. Os dados que ficam com um número a mais do determinado são os outliers.
- Para tratar, podemos remover esses pontos ou substituí-los, vai depender da aplicação utilizada. 
---

### Como concatenar vários DataFrames (empilhando linhas ou colunas),mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

```python
import pandas as pd

df1 = pd.DataFrame({
    'Nome': ['João', 'Maria'],
    'Idade': [25, 30]
})

df2 = pd.DataFrame({
    'Nome': ['Ana', 'Pedro'],
    'Cidade': ['São Paulo', 'Rio de Janeiro']
})

# Concatena por linhas (axis=0)
df_linhas = pd.concat([df1, df2], axis=0)
print("DataFrame concatenado por linhas:\n", df_linhas)

```
###### A saída do script Python é a seguinte:

<pre>
    Nome   Idade    Cidade
0   João   25.0     NaN
1  Maria   30.0     NaN
0    Ana   NaN      São Paulo
1  Pedro   NaN      Rio de Janeiro
</pre>
---
### Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
Usa-se a função `pd.read_csv()` para carregar o arquivo CSV e a função `df.head(n)` onde ***n*** é a quantidade de linhas que deseja retornar.

 ```python
import pandas as pd

caminho_arquivo = 'dados.csv'

# Realiza a leitura do arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo)

print("Primeiras linhas do DataFrame:")
print(df.head())

```

### Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

 - Para selecionar **colunas**, utiliza-se colchetes, pasasndo o nome da coluna que quer selecionar.
 - Para filtrar **linhas**, você cria uma condição booleana e a passa para o DataFrame dentro de colchetes. Apenas as linhas onde a condição é `True` serão retornadas.

```python
import pandas as pd

dados = {'Nome': ['Joao', 'Maria', 'Pedro', 'Bia'],
         'Idade': [25, 30, 22, 35],
         'Cidade': ['São Paulo', 'Rio', 'Fortaleza', 'São Paulo']}
df = pd.DataFrame(dados)

# Seleciona a coluna 'Idade'
coluna_idade = df['Idade']
print("Coluna Idade:", coluna_idade)

# Filtrar linhas onde 'Idade' é maior que 25
df_filtrado_idade = df[df['Idade'] > 25]
print("DataFrame filtrado (Idade > 25):", df_filtrado_idade)

# Seleciona a coluna 'Nome' apenas para as linhas onde 'Idade' é maior que 25
nomes_maiores_25 = df[df['Idade'] > 25]['Nome']
print("Nomes das pessoas com mais de 25 anos:", nomes_maiores_25)

```
### Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

Existem várias estratégias, e a escolha da melhor depende do contexto dos dados e do objetivo da análise.
 - `df.isnull()` retorna um DataFrame booleano do mesmo, indicando `True` onde há um NaN e `False` onde não há.
 - `df.dropna()` remove as linhas que contêm pelo menos um valor NaN
 - `df.fillna(valor)` preenche todos os NaNs com um valor específico 



