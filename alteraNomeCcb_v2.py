import os
import shutil

# Caminho da pasta "CCBS"
caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"

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
        
        # Verificar se há arquivos dentro da pasta atual
        if conteudo_pasta_atual:
            # Obter o nome do primeiro arquivo dentro da pasta atual
            primeiro_arquivo = conteudo_pasta_atual[0]
            
            # Copiar os últimos 6 caracteres do nome da pasta
            ultimos_6_caracteres = pasta[-6:]
            
            # Novo nome do arquivo com os últimos 6 caracteres
            novo_nome_arquivo =  primeiro_arquivo[:-6] + ultimos_6_caracteres + "_ccb_negociavel.pdf"
            
            # Caminho completo do arquivo original e do arquivo com o novo nome
            caminho_arquivo_original = os.path.join(caminho_pasta_atual, primeiro_arquivo)
            caminho_arquivo_novo = os.path.join(caminho_pasta_atual, novo_nome_arquivo)
            
            # Renomear o arquivo
            #os.rename(caminho_arquivo_original, caminho_arquivo_novo)
            
            print(f"O arquivo {primeiro_arquivo} na pasta {pasta} foi renomeado para {novo_nome_arquivo}.")
        else:
            print(f"A pasta {pasta} está vazia.")
    else:
        print(f"{pasta} não é uma pasta.")