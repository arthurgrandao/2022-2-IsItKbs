# ![Detecting Keyboard Smashing](https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/title.png)

<div align="center">
    <img src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad03/main/docs/images/logo.png" width="250"></img>
</div>

>2022-2-Squad 03 MDS - UnB 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

<br>

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

##  📑 Sumário
- [](#)
  - [📑Sumário](#sumário)
  - [🔎Visão Geral](#visão-geral)
  - [📁Diretórios](#diretórios)
  - [📝 Guia de instalação](#-guia-de-instalação)
  - [⚙Funcionalidades](#funcionalidades)
    - [is\_kbs(input\_data, analyzer, model)](#is_kbsinput_data-analyzer-model)
  - [📋Exemplos](#exemplos)
  - [👨‍💻Contribuidores](#contribuidores)
  - [©Licença](#licença)
<br>

<br>

##  🔎 Visão Geral
<li>Qual o objetivo desse software?</li>
O Is it KBS é um pacote python com funções capazes de determinar se entradas de texto são consideradas ou não keyboard smashing, sendo assim, cientistas de dados podem usar a biblioteca para auxiliá-los no processo de limpeza de bases de dados.

<br>

<li>O que é keyboard smashing?</li>
Keyboard smashing é a entrada ilógica e desordenada de dados, que acaba por comprometer a análise textual por sistemas de software.
Ex.:
<li>yyyyyy - É keyboard smashing.</li>
<li>aslkhfg - É keyboard smashing.</li>
<li>hello - Não é keyboard smashing.</li>

<br>

##  📁 Diretórios
<p>/.github <- Templates para issues e pull requests.<p>
<p>/estudos <- Projetos e scripts pequenos para treino da equipe.<p>
<p>/data <- Bases de dados utilizadas no treinamento do algoritmo.<p>
<p>/dist <- Distribuições do nosso pacote comprimidas.<p> 
<p>/docs <- Documentações, principalmente da gitpage.<p> 
<p>/isitkbs.egg-info <- Informações de empacotamento.<p> 
<p>/isitkbs <- Definição das funções que serão utilizadas pelos usuários.<p> 
<p>/models <- Modelos já treinados.<p>
<p>/notebooks <- Jupyter notebooks usados para testes de funcionalidades.<p>
<p>/src <- Scripts para tratamento de dados, feature engineering e treinamento de algoritmos.<p>


<br>

## 📝 Guia de instalação
<li>Necessário python 3 e pip.</li>
<li>Faça a instalação do nosso pacote com o pip no seu terminal python (as demais bibliotecas necessárias são instaladas  automáticamente com o comando abaixo):</li>

```
pip install isitkbs
```

<br>

##  ⚙ Funcionalidades

### is_kbs(input_data, analyzer, model)

```python
from isitkbs import *
is_kbs(input_data, analyzer, model)
```

- input_data: dados de entrada representados por uma string
- analyzer='word': análise de uma palavra (retorna positivo(1) ou negativo (0) se é keyboard smashing)
- analyzer='phrases': retorna quais palavras são keyboard smashing de uma frase de entrada
- model: modelo utilizado ('randomForest' por padrão)

<br>

Para novas versões, a ideia é desenvolver features que auxiliam no tratamento de keyboard smashing em textos, banco de dados, entre outros.

##  📋 Exemplos

```python
is_kbs('yyyyyy')
1
```
```python
is_kbs('Hello')
0
```

```python
is_kbs('Hello world', analyzer='phrases')
0
```

```python
is_kbs('aspdo asocjn', analyzer='phrases')
[['audhsuh'], ['hhh'], ['hhu'], ['uhauuh']]
```
<br>

##  👨‍💻 Contribuidores
[Arthur de Melo](https://github.com/arthurmlv)

[Arthur Grandão](https://github.com/arthurgrandao)

[Douglas Alves](https://github.com/dougAlvs)

[Gabriel Campello](https://github.com/g16c)

[Paulo Victor](https://github.com/PauloVictorFS)

[Rafael Ferreira](https://github.com/RafaelCLG0)

[Sidney Fernando](https://github.com/nando3d3)
<br>

##  ©Licença

This software is licensed under the [MIT](https://github.com/nhn/tui.editor/blob/master/LICENSE) ©
