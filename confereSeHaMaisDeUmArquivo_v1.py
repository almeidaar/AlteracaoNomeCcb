import os
import shutil

# Caminho da pasta "CCBS"
caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"

# Caminho para onde os arquivos .pdf serão movidos
caminho_destino = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis"

# Lista para armazenar pastas com mais de 1 arquivo
pastas_com_mais_de_um_arquivo = []

# Listar conteúdo da pasta "CCBS"
conteudo_ccbs = os.listdir(caminho_ccbs)

# Iterar sobre o conteúdo da pasta "CCBS"
for pasta in conteudo_ccbs:
    # Caminho completo da pasta atual
    caminho_pasta_atual = os.path.join(caminho_ccbs, pasta)

    # Verificar se é uma pasta
    if os.path.isdir(caminho_pasta_atual):
        # Listar conteúdo da pasta atual
        conteudo_pasta_atual = os.listdir(caminho_pasta_atual)

        # Contar o número de arquivos na pasta atual
        numero_arquivos = len(conteudo_pasta_atual)

        # Se a pasta tiver mais de 1 arquivo, adicionar à lista
        if numero_arquivos > 1:
            pastas_com_mais_de_um_arquivo.append(pasta)

# Imprimir as pastas com mais de 1 arquivo
if pastas_com_mais_de_um_arquivo:
    print("As seguintes pastas possuem mais de 1 arquivo:")
    for pasta in pastas_com_mais_de_um_arquivo:
        print(f"- {pasta}")
else:
    print("Nenhuma pasta possui mais de 1 arquivo.")
