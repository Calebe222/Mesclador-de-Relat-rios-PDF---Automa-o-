import os
from PyPDF2 import PdfMerger
from natsort import natsorted # Essa biblioteca garante a ordem 1, 2, 3... 10, 11

def mesclar_relatorios_ordenados(pasta_origem, nome_saida):
    merger = PdfMerger()
    
    # Pega os arquivos PDF
    arquivos = [f for f in os.listdir(pasta_origem) if f.lower().endswith('.pdf')]
    
    # ORDENAÇÃO NATURAL: Aqui está o segredo! 
    # Ela entende que 2 vem antes de 10.
    arquivos_ordenados = natsorted(arquivos)

    if not arquivos_ordenados:
        print("❌ Nenhum PDF encontrado.")
        return

    print("--- ORDEM DE JUNÇÃO ---")
    for arquivo in arquivos_ordenados:
        caminho_completo = os.path.join(pasta_origem, arquivo)
        merger.append(caminho_completo)
        print(f"✅ Incluído: {arquivo}")

    merger.write(nome_saida)
    merger.close()
    print(f"\n🚀 Finalizado! Arquivo '{nome_saida}' gerado com sucesso.")

# --- AJUSTE AQUI ---
# Coloque o nome da pasta onde estão esses arquivos da imagem
pasta_dos_relatorios = "rC:\Caminho\Para\Sua\Pasta" 

if os.path.exists(pasta_dos_relatorios):
    mesclar_relatorios_ordenados(pasta_dos_relatorios, "Relatorio_Anual_UFRR_Completo.pdf")
else:
    print(f"⚠️ A pasta '{pasta_dos_relatorios}' não foi encontrada.")