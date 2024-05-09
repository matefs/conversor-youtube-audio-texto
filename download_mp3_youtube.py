import pytube as pt
import os


yt = pt.YouTube("https://www.youtube.com/watch?v=FjHGZj2IjBk")
t = yt.streams.filter(only_audio=True)
t[0].download()
print(t[0])


# Listar todos os arquivos na pasta atual
arquivos = os.listdir()

# Iterar sobre os arquivos
for arquivo in arquivos:
    # Verificar se é um arquivo .mp4
    if arquivo.endswith('.mp4'):
        # Renomear para .mp3
        novo_nome = arquivo[:-4] + '.mp3'
        os.rename(arquivo, novo_nome)
