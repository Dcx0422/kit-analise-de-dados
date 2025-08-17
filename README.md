# Kit de Ferramentas do Analista de Dados

Este repositório contém um módulo Python (`ferramentas_analista.py`) projetado para resolver dores comuns e acelerar o fluxo de trabalho de analistas de dados que usam Python, especialmente com Pandas e Jupyter Notebooks.

A inspiração veio da facilidade de ferramentas como o Power Query, que inspecionam e carregam dados de forma inteligente, e da necessidade de transformar análises exploratórias em scripts reutilizáveis e documentados.

## ✨ Por que usar o Kit do Analista?

Embora as bibliotecas usadas (Pandas, Chardet, etc.) já existam, o valor desta ferramenta está na **combinação sinérgica e na filosofia focada no analista**, criando uma experiência superior à utilização das peças separadamente.

-   **Filosofia "Zero Configuração":** Assim como no Power Query, o objetivo é que você "aponte para o arquivo e comece a trabalhar". A função `carregar_dados` lida com a complexidade de detectar formatos, delimitadores, codificações e até erros estruturais, para que você não precise.

-   **Foco no Fluxo de Trabalho Completo:** O kit oferece soluções para o **início** da análise (com uma carga de dados robusta e universal) e para o **final** (com a conversão inteligente do notebook para um script `.py` de produção), acompanhando o analista de ponta a ponta.

-   **Resiliência a Dados do Mundo Real:** A carga de CSVs não apenas falha de forma graciosa, mas entra em um **modo de recuperação automático**, separando as linhas boas das ruins e salvando as problemáticas em um arquivo `_erros.csv` para inspeção. Você nunca perde dados e é sempre informado sobre a qualidade do arquivo de origem.

-   **Conversor de Notebook Inteligente:** Diferente do `nbconvert` padrão, nosso conversor foi projetado para gerar um código `.py` **altamente legível**, transformando o texto em Markdown em blocos de comentários bem formatados e neutralizando comandos específicos do Jupyter, o que facilita a manutenção e o compartilhamento do script final.

## 🚀 Funcionalidades Principais

1.  **Carregador de Dados Universal (`carregar_dados`)**
    -   Lida nativamente com os formatos mais comuns: **CSV, TXT, Excel, JSON e Parquet**.
    -   Para arquivos CSV/Texto, detecta automaticamente o delimitador e a codificação de caracteres.
    -   Possui um **modo de recuperação automático** para arquivos CSV malformados: ele carrega as linhas válidas e salva as problemáticas em um arquivo `_erros.csv` separado para inspeção.
    -   Para arquivos JSON, detecta e "achata" (normaliza) estruturas de API comuns automaticamente.

2.  **Conversor de Notebook para Script (`converter_notebook_para_py`)**
    -   Transforma seu trabalho de exploração (`.ipynb`) em um script de produção (`.py`) com um único comando.
    -   Converte suas explicações em células de **Markdown para comentários**, preservando a documentação.
    -   Identifica, neutraliza e reporta comandos específicos do Jupyter (`%matplotlib`, `!pip`, `display()`, etc.) para garantir que o script final seja 100% executável.


## 🛠️ Ambientes Suportados e Como Usar

### 1. Pré-requisitos

Primeiro, garanta que todas as dependências estejam instaladas no seu ambiente Python:


```bash
pip install pandas chardet nbformat matplotlib seaborn jupyter openpyxl pyarrowr
```

### 2. Estrutura do Projeto

Coloque o arquivo `ferramentas_analista.py`, seus notebooks e seus arquivos de dados na mesma pasta para um início rápido.

```
kit-do-analista/
├── ferramentas_analista.py
├── Analise_Exploratoria_Completa.ipynb
├── notebook_modelo.ipynb
├── ...seus arquivos de dados...
└── README.md
```

### 3. Executando a Análise

Você pode usar o `notebook_modelo.ipynb` como ponto de partida no seu ambiente preferido:

**Opção A: Jupyter Notebook Clássico (no Navegador)**

1.  Abra o terminal na pasta do projeto.
2.  Execute o comando:
    ```
    jupyter notebook
    ```
3.  No seu navegador, clique no arquivo `notebook_modelo.ipynb` para abri-lo.

**Opção B: Visual Studio Code + Extensão Jupyter (Recomendado)**

1.  **Instale as Extensões:** Na aba de Extensões (Ctrl+Shift+X) do VS Code, instale as extensões `Python` e `Jupyter` da Microsoft.
2.  **Abra a Pasta:** Vá em `Arquivo` > `Abrir Pasta...` (ou `File` > `Open Folder...`) e selecione a pasta do seu projeto.
3.  **Selecione o Kernel:** Abra o arquivo `notebook_modelo.ipynb`. No canto superior direito, clique em "Selecionar Kernel" (`Select Kernel`) e escolha o ambiente Python onde você instalou as bibliotecas.
4.  **Execute as Células:** Agora você pode executar cada célula usando o botão de "play" ou `Shift + Enter`.

## ✨ Demonstração Rápida

**Carregando um arquivo CSV malformado *sem esforço*:**

```python
# Em uma célula do notebook:
from ferramentas_analista import carregar_dados

# Apenas aponte para o arquivo!
df = carregar_dados('dados_clientes_malformado.csv')

```

**Saída esperada, mostrando a recuperação automática:**

```

--- 🕵️‍♂️ Analisando e Carregando: dados_clientes_malformado.csv ---
-> Formato CSV/Texto detectado. Iniciando análise de estrutura...

Codificação provável: 'ascii' (Confiança: 100.00%)

Delimitador provável: ','
-> Tentando carregar o arquivo no modo rápido...

⚠️  AVISO: O modo rápido falhou. O arquivo contém linhas malformadas.
Detalhe do erro: Expected 4 fields in line 4, saw 5
-> Ativando modo de segurança: separando linhas boas e ruins...

Encontradas 2 linhas problemáticas. Salvando em 'dados_clientes_malformado_erros.csv'
--- ✅ DataFrame carregado com 4 linhas! ---

```

O analista recebe o DataFrame com os dados bons e um arquivo `_erros.csv` para inspecionar, tudo automaticamente.

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