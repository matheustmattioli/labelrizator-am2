# Trabalho 1 - Classificação Multirrótulo

## Introdução

Neste repositório vamos resolver o primeiro trabalho prático da disciplina Aprendizado de Máquina 2, ofertada pelo Prof. Dr. Diego Furtado Silva
na modalidade EAD no semestre 2021/2 pelo [DC-UFSCar](https://site.dc.ufscar.br/).

Trabalho realizado pelos alunos:
- [Gabriel Penajo de Machado](https://github.com/gabrielpenajo) 
- [Matheus Ramos de Carvalho](https://github.com/OakBranches)
- [Matheus Teixeira Mattioli](https://github.com/matheustmattioli)

Segundo o enunciado deste trabalho prático, devemos escolher um tema entre as seguintes opções:
- Aprendizado semissupervisionado (incluindo OCC e PUL)
- Classificação multirrótulo
- Classificação hierárquica
- Meta-aprendizado
- Classificação em fluxo de dados
- Combinação de classificadores (heterogêneos)
- Aprendizado ativo
 
dos quais escolhemos abordar a classificação multirrótulo. A partir dessa escolha, utilizamos três algoritmos de classificação multirrótulo para solucionar cinco conjuntos de dados estruturados distintos, então elaboramos uma avaliação experimental comparativa entre os métodos implementados, a fim de testar a robustez dos algoritmos escolhidos. 

## Datasets

Os conjuntos de dados utilizados foram retirados do site [Mulan-Sourceforge](http://mulan.sourceforge.net/datasets-mlc.html
) e são:
- [Birds](https://ieeexplore.ieee.org/abstract/document/6661934).
- [Yeast](https://www.semanticscholar.org/paper/Kernel-methods-for-Multi-labelled-classification-Elisseeff-Weston/44605f6bd423852eb7c1a62004db72875fd971c9).
- [Flags](https://ieeexplore.ieee.org/abstract/document/6735287).
- [Genbase](https://link.springer.com/chapter/10.1007/11573036_42).
- [Emotions](http://mlkd.csd.auth.gr/publication_details.asp?publicationID=269).

Nas próximas subseções os *datasets* são apresentados com mais detalhes.

### *Birds*

No conjunto de dados *birds* queremos categorizar áudios captados na natureza produzidos por pássaros com as respectivas espécies de pássaros que podem produzir este som. Este *dataset* apresenta 645 instâncias e 260 atributos, sendo 2 nominais e 258 numéricos. Apresenta 19 rótulos.

### *Yeast*

No contexto de bio-informática, o *dataset Yeast* apresenta genomas de leveduras e queremos classificar leveduras de acordo com as funcionalidades geradas por essas proteínas (genes). No *dataset* existem 2417 instâncias de leveduras com 103 atributos numéricos e 14 possibilidades de classificação multirrótulo.

### *Flags*

O conjunto de dados *Flags* nos apresenta formas geométricas, cores, religião, idioma, tamanho da população, continente, entre outras informações, e pede para indicarmos quais cores a bandeira do país apresenta, sendo 7 possibilidades de cores e portanto, rótulos. Além disso, apresenta 194 instâncias e 19 atributos, com 9 nominais e 10 numéricos.


### *Genbase*

Também no contexto de bio-informática, o *dataset Genbase* apresenta sequências de proteína, genes, e pede para indicarmos as características relacionados com essa sequência do DNA. Há 662 instâncias para serem analisadas com 1186 atributos nominais e 27 rótulos representando as características do gene. 


### *Emotions*

O último *dataset* escolhido foi o *Emotions*. Queremos detectar as emoções contidas em pedaços de músicas, todos os dados já estão representados de forma numérica e estruturados. São utilizados 593 instâncias de músicas, com 72 atributos numéricos e 6 *labels*, que representam as emoções. 

## Algoritmos aplicados

Para atacar esses problemas multirrótulos, além de um pré-processamento necessário, escolhemos três algoritmos multirrótulos de classificação, que atuam transformando a natureza do problema para apenas um rótulo. São eles:
- *Binary Relevance* (BR)
- *Classifier Chains* (CC)
- *Label Powerset* (LP)

A partir disso utilizamos algoritmos de classificação para classificar os conjuntos de treino, escolhendo os melhores parâmetros através de *Grind Search* e método do cotovelo. Avaliamos a qualidade das respostas com análise de acurácia e *Hamming loss*.

## Implementação

Selecionamos os *datasets* e dividimos em conjuntos de treino e teste. Fizemos os pré-processamentos adequados e rodamos algoritmos multirrótulos, classificamos e testamos a qualidade das soluções na sequência.

## Resultados

Os resultados podem ser conferidos nos Notebooks presentes no github.

## Conclusão

Podemos dizer que o experimento proposto pelo primeiro trabalho prático de AM2 foi realizado com sucesso, já que conseguimos resolver problemas multirrótulos e avaliar e comparar as respostas obtidas, testando a robustez dos algoritmos escolhidos para esses conjuntos de dados.


