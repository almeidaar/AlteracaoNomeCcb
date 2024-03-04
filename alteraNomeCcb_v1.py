# import pandas as pd
# import os

# pasta_ccbs = os.listdir(r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS")
# print(pasta_ccbs)

# for arquivo in pasta_ccbs:
#     if "ccb" in arquivo.lower():
#         numero = pd.

import os

# Caminho da pasta "CCBS"
caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"

# Listar conteúdo da pasta "CCBS"
conteudo_ccbs = os.listdir(caminho_ccbs)

# Verificar se há pastas dentro de "CCBS"
if conteudo_ccbs:
    # Obter o nome da primeira pasta dentro de "CCBS"
    primeira_pasta = conteudo_ccbs[0]
    
    # Copiar os últimos 6 caracteres do nome da primeira pasta
    ultimos_6_caracteres = primeira_pasta[-6:]
    
    # Caminho completo da primeira pasta
    caminho_primeira_pasta = os.path.join(caminho_ccbs, primeira_pasta)
    
    # Listar conteúdo da primeira pasta
    conteudo_primeira_pasta = os.listdir(caminho_primeira_pasta)
    
    # Verificar se há arquivos dentro da primeira pasta
    if conteudo_primeira_pasta:
        # Obter o nome do primeiro arquivo
        primeiro_arquivo = conteudo_primeira_pasta[0]
        
        # Novo nome do arquivo com os últimos 6 caracteres
        novo_nome_arquivo =  primeiro_arquivo[:-6] + ultimos_6_caracteres + ".pdf"
        
        # Caminho completo do arquivo original e do arquivo com o novo nome
        caminho_arquivo_original = os.path.join(caminho_primeira_pasta, primeiro_arquivo)
        caminho_arquivo_novo = os.path.join(caminho_primeira_pasta, novo_nome_arquivo)
        
        # Renomear o arquivo
        os.rename(caminho_arquivo_original, caminho_arquivo_novo)
        
        print(f"O arquivo {primeiro_arquivo} foi renomeado para {novo_nome_arquivo}.")
    else:
        print("Não há arquivos dentro da primeira pasta.")
else:
    print("A pasta CCBS está vazia.")
