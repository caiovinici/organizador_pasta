import os
from tkinter.filedialog import askdirectory
#
caminho = askdirectory(title='Selecione uma pasta') # opc de escolher pasta
lista_arquivos = os.listdir(caminho) # 
#
locais = { # dicionario criado
    'imagens': ['.png', '.jpg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
    'aplicativos': ['.exe'],
}
for arquivo in lista_arquivos:
    # nomo do arq+.png
    nome,extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}',f'{caminho}/{pasta}/{arquivo}')
