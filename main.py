from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def raiz(request: Request):
    video_url = request.query_params.get("video_url")
    if video_url is not None:
        return {"video_url": f"{video_url}!"}
    else:
        return {"mensagem": "Por favor, informe uma URL do YouTube no parâmetro /?video_url="}
