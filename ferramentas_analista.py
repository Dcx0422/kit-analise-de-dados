"""
Kit de Ferramentas do Analista de Dados
---------------------------------------

Este módulo fornece um conjunto de funções para agilizar o fluxo de
trabalho de análise de dados, desde a importação inteligente de dados
de múltiplos formatos até a conversão de notebooks para scripts.
"""

import pandas as pd
import chardet
import csv
import io
import nbformat
import sys
import os

# ==============================================================================
# FUNÇÃO 1: CARREGADOR DE DADOS UNIVERSAL (COM MODO DE RECUPERAÇÃO AUTOMÁTICO)
# ==============================================================================

def _carregar_csv_inteligente(caminho_arquivo: str):
    """
    Função interna para a lógica de detecção e carga de CSV.
    Agora com um modo de recuperação automático para arquivos malformados.
    """
    print("-> Formato CSV/Texto detectado. Iniciando análise de estrutura...")
    
    # --- Passo 1: Detectar estrutura (codificação e delimitador) ---
    try:
        with open(caminho_arquivo, 'rb') as f:
            raw_data = f.read(20000)
        
        resultado_chardet = chardet.detect(raw_data)
        codificacao = resultado_chardet['encoding'] or 'utf-8'
        print(f"   - Codificação provável: '{codificacao}' (Confiança: {resultado_chardet['confidence']:.2%})")

        amostra_texto = raw_data.decode(codificacao, errors='ignore')
        delimitador = ','
        try:
            dialect = csv.Sniffer().sniff(amostra_texto, delimiters=',;|\t')
            delimitador = dialect.delimiter
            print(f"   - Delimitador provável: '{delimitador}'")
        except csv.Error:
            print("   - Não foi possível detectar o delimitador. Usando ',' (vírgula).")

    except Exception as e:
        print(f"❌ ERRO na fase de detecção: {e}")
        return None

    # --- Passo 2: Tentativa de Carga Rápida ---
    try:
        print("-> Tentando carregar o arquivo no modo rápido...")
        df = pd.read_csv(caminho_arquivo, sep=delimitador, encoding=codificacao, engine='python', on_bad_lines='error')
        return df
    
    # --- Passo 3: Modo de Recuperação Automático ---
    except pd.errors.ParserError as e:
        print(f"   - ⚠️  AVISO: O modo rápido falhou. O arquivo contém linhas malformadas.")
        print(f"      Detalhe do erro: {e}")
        print("-> Ativando modo de segurança: separando linhas boas e ruins...")

        try:
            linhas_boas = []
            linhas_ruins = []
            
            with open(caminho_arquivo, 'r', encoding=codificacao, errors='ignore') as f:
                leitor_csv = csv.reader(f, delimiter=delimitador)
                
                # Lê o cabeçalho para determinar o número esperado de colunas
                cabecalho = next(leitor_csv)
                num_colunas_esperado = len(cabecalho)
                linhas_boas.append(cabecalho)
                
                # Itera sobre o restante do arquivo
                for i, linha in enumerate(leitor_csv, start=2): # start=2 para contar a linha do cabeçalho
                    if len(linha) == num_colunas_esperado:
                        linhas_boas.append(linha)
                    else:
                        # Adiciona a linha original (texto) e o número da linha ao log de erros
                        linhas_ruins.append([i, f"Esperava {num_colunas_esperado} colunas, encontrou {len(linha)}", str(linha)])

            # Salva as linhas problemáticas em um arquivo de log/erros
            if linhas_ruins:
                caminho_erros = f"{os.path.splitext(caminho_arquivo)[0]}_erros.csv"
                print(f"   - Encontradas {len(linhas_ruins)} linhas problemáticas. Salvando em '{os.path.basename(caminho_erros)}'")
                
                with open(caminho_erros, 'w', newline='', encoding='utf-8') as f_erros:
                    escritor = csv.writer(f_erros)
                    escritor.writerow(['Numero_Linha_Original', 'Problema', 'Conteudo_Linha'])
                    escritor.writerows(linhas_ruins)

            # Cria o DataFrame final a partir das linhas boas
            if len(linhas_boas) > 1: # Se encontrou mais do que apenas o cabeçalho
                df = pd.DataFrame(linhas_boas[1:], columns=linhas_boas[0])
                # Tenta converter os tipos de dados automaticamente, como o read_csv faz
                df = df.infer_objects() 
                return df
            else:
                print("❌ ERRO: Nenhuma linha de dados válida foi encontrada após a limpeza.")
                return None

        except Exception as e_safe:
            print(f"❌ ERRO: O modo de segurança também falhou: {e_safe}")
            return None


def carregar_dados(caminho_arquivo: str, **kwargs):
    """
    Carrega dados de diferentes tipos de arquivos (CSV, Excel, JSON, Parquet).
    Para CSVs, usa um modo de recuperação automático para lidar com linhas malformadas.
    """
    print(f"--- 🕵️‍♂️ Analisando e Carregando: {os.path.basename(caminho_arquivo)} ---")
    
    # ... (o resto da função permanece o mesmo, chamando a nova lógica para CSV)
    if not os.path.exists(caminho_arquivo):
        print(f"❌ ERRO: Arquivo não encontrado em '{caminho_arquivo}'")
        return None

    df = None
    try:
        _, extensao = os.path.splitext(caminho_arquivo)
        extensao = extensao.lower()

        if extensao in ['.csv', '.txt', '.tsv']:
            df = _carregar_csv_inteligente(caminho_arquivo)
        
        elif extensao in ['.xlsx', '.xls']:
            print("-> Formato Excel detectado. Usando 'pd.read_excel'.")
            df = pd.read_excel(caminho_arquivo, **kwargs)
        
        elif extensao == '.json':
            print("-> Formato JSON detectado. Usando 'pd.read_json'.")
            df = pd.read_json(caminho_arquivo, **kwargs)
            
        elif extensao == '.parquet':
            print("-> Formato Parquet detectado. Usando 'pd.read_parquet'.")
            df = pd.read_parquet(caminho_arquivo, **kwargs)
            
        else:
            print(f"❌ ERRO: Tipo de arquivo '{extensao}' não é suportado.")
            return None
        
        if df is not None:
            print(f"--- ✅ DataFrame carregado com {len(df)} linhas! ---")
        
        return df

    except Exception as e:
        print(f"❌ ERRO inesperado ao carregar o arquivo: {e}")
        return None

# ==============================================================================
# FUNÇÃO 2: CONVERSOR DE NOTEBOOK (Sem alterações)
# ==============================================================================
def converter_notebook_para_py(caminho_notebook: str, caminho_script_saida: str | None = None):
    # (O código desta função permanece exatamente o mesmo da versão anterior)
    if not caminho_notebook.endswith('.ipynb'):
        print("❌ ERRO: O arquivo de entrada deve ser um Jupyter Notebook (.ipynb)")
        return
    if caminho_script_saida is None:
        caminho_script_saida = caminho_notebook.replace('.ipynb', '.py')
    print(f"\n--- 🔄 Convertendo '{caminho_notebook}' para '{caminho_script_saida}' ---")

    try:
        with open(caminho_notebook, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        script_python = [
            "# -*- coding: utf-8 -*-",
            '"""',
            f"Script gerado automaticamente a partir de {os.path.basename(caminho_notebook)}",
            '"""',
            ""
        ]
        
        comandos_jupyter_encontrados = set()

        for cell in notebook.cells:
            if cell.cell_type == 'code':
                codigo_limpo = []
                linhas_codigo = cell.source.split('\n')
                
                for i, linha in enumerate(linhas_codigo):
                    linha_strip = linha.strip()
                    linha_processada = linha

                    if 'display(' in linha:
                        linha_processada = linha.replace('display(', 'print(', 1)
                        if '#' not in linha_processada:
                            linha_processada += " # Convertido de display() para print()"
                        comandos_jupyter_encontrados.add('display()')
                    
                    elif linha_strip.startswith('%'):
                        comando_magico = linha_strip.split(' ')[0]
                        comandos_jupyter_encontrados.add(comando_magico)
                        linha_processada = f"# {linha}"
                    
                    elif linha_strip.startswith('!'):
                        comando_shell = "!" + linha_strip[1:].split(' ')[0]
                        comandos_jupyter_encontrados.add(comando_shell)
                        linha_processada = f"# {linha}"
                    
                    codigo_limpo.append(linha_processada)
                
                script_python.extend(["\n# --- Célula de Código ---", *codigo_limpo, "\n"])

            elif cell.cell_type == 'markdown':
                script_python.append("#" + "="*78)
                linhas_markdown = [f"# {linha}" for linha in cell.source.split('\n')]
                script_python.extend(["# CÉLULA DE MARKDOWN", *linhas_markdown])
                script_python.append("#" + "="*78 + "\n")

        with open(caminho_script_saida, 'w', encoding='utf-8') as f:
            f.write("\n".join(script_python))

        print(f"--- ✅ Conversão concluída! Arquivo salvo em: '{caminho_script_saida}' ---")

        if comandos_jupyter_encontrados:
            print("\n" + "="*50)
            print("⚠️  RELATÓRIO DE COMPATIBILIDADE")
            print("="*50)
            print("Seu notebook continha comandos específicos do Jupyter que não")
            print("funcionam em scripts .py. Eles foram tratados da seguinte forma:")
            
            for cmd in sorted(list(comandos_jupyter_encontrados)):
                if cmd == 'display()':
                    print(f"   - [CONVERTIDO] '{cmd}': Substituído pela função 'print()'.")
                else:
                    print(f"   - [COMENTADO]  '{cmd}': A linha de comando foi mantida, mas desativada com '#'.")
            print("="*50)

    except FileNotFoundError:
        print(f"❌ ERRO: Notebook '{caminho_notebook}' não encontrado.")
    except Exception as e:
        print(f"❌ ERRO: Problema inesperado durante a conversão: {e}")