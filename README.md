# Tokenizer API
This is an API for [Tokenizer](https://github.com/mideind/Tokenizer) using the [ELG specification](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern).
The API is wrapped in a [docker container](https://www.docker.com/) and is implemented using [fastapi](https://github.com/tiangolo/fastapi).

# Getting started
Running ./run.sh will build and run the docker container

# API calls
All the API calls use post and input/outputs are in a json format.
Further details about the api calls are automatically generated when the container is run and can be found in /docs or /redoc

| HTTP METHOD | Description |
| ----------- | --------------- |
| /tokenizer | Takes in text and splits them up into tokens |
| /tokenizer/impl | Same as /tokenizer but for testing purposes |

# Author

[Reykjavik University](https://lvl.ru.is)

Jökull Snær Gylfason

# Acknowledgements
