import os
import shutil

caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"
caminho_destino = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis"

conteudo_ccbs = os.listdir(caminho_ccbs)

for arquivo in conteudo_ccbs:
    caminho_arquivo_atual = os.path.join(caminho_ccbs, arquivo)
    
    if os.path.isfile(caminho_arquivo_atual):  # Verifica se é um arquivo
        primeiros_6_caracteres = arquivo[:6]  # Pegando os 6 primeiros caracteres do nome do arquivo
        
        novo_nome_arquivo = primeiros_6_caracteres + os.path.splitext(arquivo)[1]  # Novo nome do arquivo
        
        caminho_arquivo_novo = os.path.join(caminho_ccbs, novo_nome_arquivo)
        
        os.rename(caminho_arquivo_atual, caminho_arquivo_novo)
        
        print(f"O arquivo {arquivo} foi renomeado para {novo_nome_arquivo}.")
        
        if caminho_arquivo_novo.endswith('.pdf'):
            shutil.move(caminho_arquivo_novo, caminho_destino)
            print(f"O arquivo {novo_nome_arquivo} foi movido para {caminho_destino}.")
