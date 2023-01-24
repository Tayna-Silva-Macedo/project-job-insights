# Bem-vindo ao Projeto Job Insights!

Este é um projeto da [Trybe](https://www.betrybe.com/) que foi desenvolvido no módulo de Ciência da Computação.
O Job Insights é um site que permite a consulta de dados sobre empregos. Estes dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma que disponibiliza conjuntos de dados para cientistas de dados.

![job](https://user-images.githubusercontent.com/99992183/214390151-5f208766-dbd7-4ac4-bc2f-299e1f7a04e0.png)


## Tecnologias utilizadas

Em seu desenvolvimento foi utilizada linguagem ***Python*** para escrever os códigos e ***Flask***, um framework web muito popular na comunidade Python para o desenvolvimento web. 

Fora isso, foi utilizado o framework ***pytest***, para testar implementações já fornecidas pela Trybe.

## Habilidades que foram trabalhadas:

  - Utilização do terminal interativo do Python; 
  - Utilização de estruturas condicionais e de repetição;
  - Utilização de funções built-in do Python;
  - Tratamento de exceções;
  - Manipulação de arquivos;
  - Escrita de funções;
  - Escrita de testes com Pytest;
  - Escrita de módulos, bem como sua importação em outros códigos.

## Como rodar o projeto na sua máquina:

1. Navegue até o local onde deseja clonar o repositório e utilize o **git clone**:
```
git clone git@github.com:Tayna-Silva-Macedo/project-job-insights.git
```

2. Acesse o diretório do projeto **project-job-insights**:
```
cd project-job-insights
```

3. Crie e ative um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Rode a aplicação Flask:
```
flask run
```

> ℹ️ Depois de subir a aplicação, é possível acessar o site gerado pelo Flask em http://localhost:5000.

6. Para rodar os testes é utilizado o seguinte comando:

```
python3 -m pytest
```
