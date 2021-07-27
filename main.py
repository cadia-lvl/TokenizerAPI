
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse

from tokenizer import split_into_sentences
from pydantic import BaseModel

__version__ = 0.1

app = FastAPI()

class TokenizerInput(BaseModel):
    type: str = "text"
    content: str

@app.get('/', response_class=HTMLResponse)
def home() -> str:
    return """
<html>
    <head><title>Tokenizer API</title></head>
    <body>
        <h1>Greynir API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(__version__)

@app.post('tokenize')
def tokenize(request: TokenizerInput):
    return tokenize_impl(request.content)

@app.post('/tokenize/impl')
def tokenize_impl(text : str) -> JSONResponse:
    g = split_into_sentences(text)
    content = []
    for sentence in g:
        tokens = sentence.split()
        content.append(tokens)
    response = {"response":{
                "type":"texts",
                "content":content
            }}
    return JSONResponse(content=response)
