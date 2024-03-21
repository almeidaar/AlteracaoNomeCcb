import os
import shutil

caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"
caminho_destino = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis"

conteudo_ccbs = os.listdir(caminho_ccbs)

nome_ccb = "_ccb_negociavel.pdf"

for arquivo in conteudo_ccbs:
    caminho_pasta_atual = os.path.join(caminho_ccbs)
    
    if os.path.isdir(caminho_pasta_atual):
        conteudo_pasta_atual = os.listdir(caminho_pasta_atual)
        
        for item in conteudo_pasta_atual:
            caminho_item_atual = os.path.join(caminho_pasta_atual)
            
            if os.path.isfile(caminho_item_atual):  # Verifica se é um arquivo
                primeiros_6_caracteres = arquivo[:6]  # Pegando os 6 primeiros caracteres da pasta
                
                novo_nome_arquivo = item  # Novo nome do arquivo
                
                caminho_arquivo_original = caminho_item_atual
                caminho_arquivo_novo = os.path.join(caminho_pasta_atual, novo_nome_arquivo)
                
                os.rename(caminho_arquivo_original, caminho_arquivo_novo)
                
                print(f"O arquivo {item} na pasta {arquivo} foi renomeado para {novo_nome_arquivo}.")
                
                if caminho_arquivo_novo.endswith('.pdf'):
                    shutil.move(caminho_arquivo_novo, caminho_destino)
                    print(f"O arquivo {novo_nome_arquivo} foi movido para {caminho_destino}.")
