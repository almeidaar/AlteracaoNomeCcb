import os
import shutil


caminho_ccbs = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis\CCBS"

caminho_destino = r"C:\Users\NicholasAlmeidaRodri\MEUCASHCARD SERVIÇOS TECNOLOGICOS E FINANCEIROS LTDA\Engenharia de Dados - Integracao Solis"

conteudo_ccbs = os.listdir(caminho_ccbs)

nome_ccb = "_ccb_negociavel.pdf"

for pasta in conteudo_ccbs:
    
    caminho_pasta_atual = os.path.join(caminho_ccbs, pasta)
        
    if os.path.isdir(caminho_pasta_atual):
        
        conteudo_pasta_atual = os.listdir(caminho_pasta_atual)
                
        if conteudo_pasta_atual:
            
            primeiro_arquivo = conteudo_pasta_atual[0]
                        
            ultimos_6_caracteres = pasta[-6:]
                        
            novo_nome_arquivo =  primeiro_arquivo[27:] + ultimos_6_caracteres + "_ccb_negociavel.pdf"
                        
            caminho_arquivo_original = os.path.join(caminho_pasta_atual, primeiro_arquivo)
            caminho_arquivo_novo = os.path.join(caminho_pasta_atual, novo_nome_arquivo)
                        
            os.rename(caminho_arquivo_original, caminho_arquivo_novo)
            
            print(f"O arquivo {primeiro_arquivo} na pasta {pasta} foi renomeado para {novo_nome_arquivo}.")
                    
            if caminho_arquivo_novo.endswith('.pdf'):
                
                shutil.move(caminho_arquivo_novo, caminho_destino)
                print(f"O arquivo {novo_nome_arquivo} foi movido para {caminho_destino}.")
                
        os.chdir(caminho_ccbs)