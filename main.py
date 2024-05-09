from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def raiz(request: Request):
    nome = request.query_params.get("nome")
    if nome is not None:
        return {"mensagem": f"Olá, {nome}!"}
    else:
        return {"mensagem": "Por favor informe uma url"}
