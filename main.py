from fastapi import FastAPI, Request
import pytube as pt
import os

app = FastAPI()
# Todo: deal with age restricted videos. Ex: https://www.youtube.com/watch?v=hsZVlDQEwnI


@app.get("/")
async def raiz(request: Request):
    video_url = request.query_params.get("video_url")
    if video_url is not None:
        yt = pt.YouTube(str(video_url))
        t = yt.streams.filter(only_audio=True)
        t[0].download()

        arquivos = os.listdir()

        for arquivo in arquivos:
            if arquivo.endswith('.mp4'):
                # Renomear para .mp3
                novo_nome = arquivo[:-4] + '.mp3'
                os.rename(arquivo, novo_nome)

        return {"video_url": f"{video_url}!", "status": "sucesso"}
    else:
        return {"mensagem": "Por favor, informe uma URL do YouTube no parâmetro /?video_url="}
