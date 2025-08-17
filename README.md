# Caixa de Ferramentas do Analista de Dados

Este repositório contém um módulo Python (`ferramentas_analista.py`) projetado para resolver duas dores comuns no fluxo de trabalho de analistas de dados que usam Python e Jupyter Notebooks.

A inspiração veio da facilidade de ferramentas como o Power Query, que inspecionam e carregam dados de forma inteligente, e da necessidade de transformar análises exploratórias em scripts reutilizáveis.

## 🚀 Funcionalidades Principais

1.  **Carregador Inteligente de CSV (`carregar_csv_inteligente`)**
    -   Chega de tentativa e erro com `pd.read_csv`!
    -   Detecta automaticamente o **delimitador** (`,` , `;` , `\t` e outros).
    -   Detecta automaticamente a **codificação de caracteres** (UTF-8, Latin-1, etc.), evitando problemas com acentuação.
    -   Exibe um resumo claro do que foi detectado antes de carregar os dados.

2.  **Conversor de Notebook para Script (`converter_notebook_para_py`)**
    -   Transforma seu trabalho de exploração (`.ipynb`) em um script de produção (`.py`) com um único comando.
    -   Mantém as células de código como código Python.
    -   Converte suas explicações em células de **Markdown para comentários**, preservando a documentação.
    -   Comenta automaticamente comandos "mágicos" (`%matplotlib inline`) que só funcionam em notebooks.

## 🛠️ Como Usar

### 1. Pré-requisitos

Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas chardet nbformat matplotlib seaborn jupyter
```

### 2. Estrutura

Para testar o projeto, clone este repositório ou baixe os arquivos e coloque-os na mesma pasta:

```
kit-do-analista/
├── ferramentas_analista.py
├── Analise_Exploratoria_Completa.ipynb
├── relatorio_vendas_BR.csv
├── dados_feedback_US.csv
├── log_acessos.tsv
└── README.md
```

### 3. Executando a Demonstração

1.  Abra o Jupyter Notebook:
    ```
    jupyter notebook
    ```
2.  Navegue até a pasta do projeto e abra o arquivo `Analise_Exploratoria_Completa.ipynb`.
3.  Execute as células uma a uma para ver a ferramenta em ação!

## ✨ Demonstração Rápida

**Carregando um arquivo complexo (padrão brasileiro) de forma simples:**

```python
# Em uma célula do notebook:
from ferramentas_analista import carregar_csv_inteligente

# Apenas aponte para o arquivo!
df_vendas = carregar_csv_inteligente('relatorio_vendas_BR.csv')
```

**Saída esperada:**
```
--- 🚀 Iniciando Análise Automática de 'relatorio_vendas_BR.csv' ---
✅ Codificação Detectada: 'ISO-8859-1' (Confiança: 73.00%)
✅ Delimitador Detectado: ';'
--- 🔄 Carregando o arquivo com os parâmetros detectados ---
--- ✅ DataFrame carregado com sucesso! ---
```

**Convertendo o notebook em um script no final da análise:**

```python
# Na última célula do notebook:
from ferramentas_analista import converter_notebook_para_py

# Apenas informe o nome do seu notebook
converter_notebook_para_py('Analise_Exploratoria.ipynb')
```

**Saída esperada:**
```
--- 🔄 Convertendo 'Analise_Exploratoria.ipynb' para 'Analise_Exploratoria.py' ---
--- ✅ Conversão concluída! Arquivo salvo em: 'Analise_Exploratoria.py' ---
```

## 🤝 Contribuição

Sinta-se à vontade para abrir *issues* com sugestões de melhoria ou fazer um *fork* do projeto e enviar um *pull request*. Toda contribuição para ajudar a comunidade de análise de dados é bem-vinda!

## 📜 Licença

Este projeto está sob a licença MIT.