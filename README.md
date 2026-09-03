<h1 align="center">
  🧮 Calculadora Básica em Python + CI/CD
</h1>

<p align="center">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/CI-GitHub_Actions-success?style=for-the-badge&logo=github-actions&logoColor=white">
  <img alt="Python 3.12" src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Pytest" src="https://img.shields.io/badge/Pytest-Testing-yellow?style=for-the-badge&logo=pytest">
</p>

<p align="center">
  Projeto desenvolvido para demonstrar a implementação de uma esteira de Integração Contínua (CI) contemplando Análise de Código (Linter), Testes Unitários, Cobertura de Código e Análise de Segurança.
</p>

<hr>

## 📑 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Pipeline de CI/CD](#-pipeline-de-cicd)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar Localmente](#-como-executar-localmente)

## 💻 Sobre o Projeto

Esta é uma aplicação modular de uma calculadora desenvolvida em **Python**. A aplicação separa cada operação matemática em funções independentes e testáveis. 

O foco principal deste repositório não é a complexidade matemática, mas sim a sua **infraestrutura de validação automatizada** utilizando o **GitHub Actions**. O projeto serve como um modelo padrão de boas práticas para integração contínua, garantindo que o código base esteja sempre funcional antes de qualquer integração.

## 📁 Estrutura do Repositório

A arquitetura do projeto foi pensada para manter o total isolamento dos testes, onde cada operação possui seu próprio script de validação:

```bash
.
├── .github/
│   └── workflows/
│       └── testes.yml         # Definição dos jobs da pipeline (Lint, Testes, Cobertura, Segurança)
├── calculadora.py             # Módulo principal com as funções matemáticas
├── test_soma.py               # Suíte de testes para adição
├── test_subtracao.py          # Suíte de testes para subtração
├── test_multiplicacao.py      # Suíte de testes para multiplicação
└── test_divisao.py            # Suíte de testes para divisão
```

## ⚙️ Pipeline de CI/CD

A esteira de Integração Contínua é ativada automaticamente a cada `push` realizado na branch `main` e atua como um portão de qualidade dividindo a validação nas seguintes etapas:

1. **Análise de Código (Linter):** Utiliza o `flake8` para garantir que o código Python segue os padrões de formatação e estilo.
   - **Matrix Strategy:** Essa etapa é executada em uma matriz que roda em diferentes versões de Sistema Operacional e do Python (3.11 e 3.12) para assegurar a compatibilidade.
2. **Testes Unitários:** Executa testes automatizados com `pytest` paralelamente em instâncias limpas do `ubuntu-latest` para validar cada operação matemática.
3. **Cobertura de Código (Coverage):** Utiliza o `pytest-cov` para analisar se **100%** do código-fonte está sendo testado.
4. **SonarQube (Quality Gate):** Ferramenta integrada ao processo para enviar o relatório de cobertura à nuvem do SonarCloud e fazer uma checagem rigorosa caçando *Bugs*, *Code Smells* e falhas de cobertura.
5. **Análise de Segurança:** Roda um scanner (Varredura de Segredos) para detectar se alguma chave de API, token ou senha foi esquecida no código, barrando o *deploy* em caso de vazamento.

> **💡 Otimização (Cache):** Toda a pipeline utiliza o mecanismo de *cache* para dependências do `pip`. Isso evita fazer download das mesmas bibliotecas em cada nova execução, deixando a esteira mais ágil e economizando recursos.

## 🛠️ Pré-requisitos

Para rodar este projeto em sua máquina local, você precisará de:
- **Python** (versão 3.12 ou superior)
- **Pip** (gerenciador de pacotes padrão do Python)
- **Git**

## 🚀 Como Executar Localmente

**1. Clone este repositório:**
```bash
git clone https://github.com/SEU-USUARIO/pipeline-calculadora.git
cd pipeline-calculadora
```

**2. Instale as dependências necessárias para os testes:**
```bash
pip install pytest
```

**3. Execute a bateria de testes:**

Para rodar **todos** os testes simultaneamente:
```bash
pytest
```

Para rodar um teste **isolado** (replicando o comportamento exato da pipeline):
```bash
pytest test_soma.py
```

<hr>
<p align="center">Desenvolvido como atividade da disciplina Integração e Entrega
Contínua.</p>
