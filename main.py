
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse

from tokenizer import split_into_sentences


__version__ = 0.1

app = FastAPI()


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

@app.get('/tokenize')
def tokenize(text : str) -> JSONResponse:
    g = split_into_sentences(text)
    out = []
    for sentence in g:
        tokens = sentence.split()
        out.append(tokens)
    return JSONResponse(content=out)
