## O que é machine learning?

Machine learning é, como se traduz, o aprendizado de máquina.  
É uma área da inteligência artificial e basicamente é como ensinar um computador a aprender com exemplos passados a ele.  
Diferente de um algoritmo comum que segue um passo a passo muito bem definido de regras que foram especificadas, o ML aprende à medida que é treinado com dados e sua saída é de certa forma "inesperada".

Quando aprendemos a programar, sempre nos fazem a analogia da receita de bolo, onde você sabe exatamente qual é a entrada e o que vai sair.  
Já no machine learning, a gente alimenta o sistema com muitos dados, e ele vai aprendendo a identificar padrões por conta própria. Com o tempo, ele consegue fazer previsões ou tomar decisões com base nesse aprendizado.

A saída do modelo não é algo que você programou diretamente, mas sim o resultado do que ele aprendeu durante o treinamento.  
Por isso, às vezes, o que ele responde pode parecer inesperado, mas é porque ele está tirando conclusões com base no que viu antes.

---

## Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning

Quando a gente treina um modelo de machine learning, a gente precisa separar os dados em três partes: treinamento, validação e testes.  

- **Conjunto de treinamento**: é como o nome diz, a etapa onde treinamos nosso modelo, onde passamos diversos dados para que ele consiga identificar padrões.
- **Conjunto de validação**: é a etapa onde verificamos como o modelo está se saindo enquanto está aprendendo, e também pra ajustar parâmetros. O importante é que esses dados não são mostrados no treinamento direto, são só pra testar o desempenho enquanto ele ainda está sendo ajustado. 
- **Conjunto de teste**: é a prova final. Depois que o modelo já foi treinado e ajustado, a gente usa esse conjunto pra ver como ele se sai com dados que ele nunca viu antes.  
  Isso mostra se o modelo realmente aprendeu algo útil ou se só "decorou" os exemplos do treino.

---

## Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento

Quando você tá lidando com dados pra treinar um modelo de machine learning, uma coisa bem comum é encontrar valores ausentes, tipo campos vazios em uma tabela.  
E isso pode atrapalhar bastante o aprendizado do modelo, então precisamos tratar esses dados antes de treinar.

- Podemos **remover essas linhas ou colunas faltantes**.
- Podemos **preencher esses valores**.
- Ou **marcar esses espaços vazios como uma categoria** para o modelo aprender que pode existir esses dados vazios (costumo não utilizar esse).

---

## O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

A **matriz de confusão** é uma forma de visualizar como um modelo está se saindo, quais acertos e erros ele cometeu ao tentar prever os resultados.

---

## Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, entre outras) você acha mais interessante aplicar algoritmos de machine learning?

A área que mais me chama atenção é a **saúde**.  
Acho muito interessante a ideia de usar machine learning pra analisar exames, interpretar documentos médicos e ajudar na parte mais operacional do sistema, sempre pensando em como isso pode beneficiar o paciente no final das contas.  
Além de tornar tudo mais rápido, pode também ajudar a evitar erros e melhorar o atendimento.

Outra área que também vejo como muito promissora é a **agricultura**.  
Dá pra usar ML pra prever colheitas, detectar pragas, saber a melhor hora de plantar ou economizar água e insumos.  
E o mais bacana é que isso pode ser adaptado pra ajudar pequenos produtores e comunidades mais carentes, levando tecnologia pra quem mais precisa.
