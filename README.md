# Organizador de Arquivos
Este é um script em Python que organiza arquivos em um diretório especificado, movendo-os para subpastas com base em suas extensões. O código é projetado para identificar arquivos de áudio, vídeo, imagem, documento e outros tipos, e organizá-los em pastas separadas.

## Funcionalidade
O script cria as seguintes subpastas dentro do diretório fornecido:

* ``áudios``: Para arquivos de áudio (extensões: .mp3, .wav)
* ``imagens``: Para arquivos de imagem (extensões: .jpg, .jpeg, .png)
* ``documentos``: Para documentos (extensões: .txt, .log, .pdf)
* ``vídeos``: Para arquivos de vídeo (extensões: .mp4, .mov, .avi)
* ``outros``: Para arquivos com extensões que não se encaixam nas categorias acima

Após a criação das pastas, o script verifica todos os arquivos no diretório especificado e move cada um para a pasta correspondente, com base na sua extensão.

## Adaptação
O código é facilmente adaptável! Basta alterar as extensões dentro das listas ``audios_ext``, ``videos_ext``, ``imagens_ext`` e ``documentos_ext`` para adicionar ou remover tipos de arquivos conforme a necessidade.