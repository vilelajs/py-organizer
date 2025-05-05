from pathlib import Path

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf']

def organizar(diretorio):
    # Cria os diretórios de destino (caso não existam)
    audios_dir = Path(diretorio, "áudios")
    audios_dir.mkdir(parents=True, exist_ok=True)

    imagens_dir = Path(diretorio, "imagens")
    imagens_dir.mkdir(parents=True, exist_ok=True)

    docs_dir = Path(diretorio, "documentos")
    docs_dir.mkdir(parents=True, exist_ok=True)

    videos_dir = Path(diretorio, "vídeos")
    videos_dir.mkdir(parents=True, exist_ok=True)

    outros_dir = Path(diretorio, "outros")
    outros_dir.mkdir(parents=True, exist_ok=True)

    diretorio = Path(diretorio)

    # Organiza os arquivos
    for arquivo in diretorio.iterdir():
        # se for um arquivo
        if arquivo.is_file():
            # Extensão do arquivo com letras minúsculas
            extensao = arquivo.suffix.lower()
            if extensao in audios_ext:
                nova_pasta = audios_dir
            elif extensao in videos_ext:
                nova_pasta = videos_dir
            elif extensao in imagens_ext:
                nova_pasta = imagens_dir
            elif extensao in documentos_ext:
                nova_pasta = docs_dir
            else:
                nova_pasta = outros_dir

            # Move o arquivo para o diretório apropriado
            novo_caminho = nova_pasta / arquivo.name
            arquivo.rename(novo_caminho)

if __name__ == '__main__':
    diretorio = input(r"Diretório: ")
    organizar(diretorio)
