# Kit de Ferramentas do Analista de Dados

Este repositório contém um módulo Python (`ferramentas_analista.py`) projetado para resolver duas dores comuns no fluxo de trabalho de analistas de dados que usam Python e Jupyter Notebooks, agilizando tarefas repetitivas.

A inspiração veio da facilidade de ferramentas como o Power Query, que inspecionam e carregam dados de forma inteligente, e da necessidade de transformar análises exploratórias em scripts reutilizáveis.

## 🚀 Funcionalidades Principais

1.  **Carregador de Dados Universal (`carregar_dados`)**
    -   Lida nativamente com os formatos mais comuns: **CSV, TXT, Excel, JSON e Parquet**.
    -   Para arquivos CSV/Texto, detecta automaticamente o delimitador e a codificação de caracteres.
    -   **Possui um modo de recuperação automático para arquivos CSV malformados:** ele carrega as linhas válidas e salva as problemáticas em um arquivo `_erros.csv` separado para inspeção, sem quebrar a execução.

2.  **Conversor de Notebook para Script (`converter_notebook_para_py`)**
    -   Transforma seu trabalho de exploração (`.ipynb`) em um script de produção (`.py`) com um único comando.
    -   Converte suas explicações em células de **Markdown para comentários**, preservando a documentação.
    -   Identifica, neutraliza e reporta comandos específicos do Jupyter (`%matplotlib`, `!pip`, `display()`, etc.) para garantir que o script final seja 100% executável.

## 🛠️ Como Usar

### 1. Pré-requisitos

Certifique-se de ter as bibliotecas necessárias instaladas para dar suporte a todos os formatos:

```bash
pip install pandas chardet nbformat matplotlib seaborn jupyter openpyxl pyarrowr
```

### 2. Estrutura

Para testar o projeto, use o notebook de demonstração `Analise_Exploratoria_Completa.ipynb` ou comece um novo projeto com o `notebook_modelo.ipynb`.

```
kit-do-analista/
├── ferramentas_analista.py
├── Analise_Exploratoria_Completa.ipynb
├── notebook_modelo.ipynb
├── ...seus arquivos de dados...
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