# Tokenizer API
This is an API for [Tokenizer](https://github.com/mideind/Tokenizer) using the [ELG specification](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern).
The API is wrapped in a [docker container](https://www.docker.com/) and is implemented using [fastapi](https://github.com/tiangolo/fastapi).

# Getting started
Running `./run.sh` will build and run the docker container

# API calls
All the API calls use post and input/outputs are in a json format, following the specification from [elg](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern).

| HTTP METHOD | Description |
| ----------- | --------------- |
| /tokenizer | Takes in text and splits them up into tokens |


# Testing

In the test folder can be found basic scripts for testing the functionality of the api.

## Testing elg

For testing if the [elg specifications](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern) are being met, you must specify which api you want to test in the `.env` file. Then you run `docker-compose up` and submit the api calls to `localhost:8080/process/service`.

# Funding
This ELG API was developed by the [language and voice labs](https://lvl.ru.is/) at [Reykjavík University](https://en.ru.is/) in EU's CEF project: [Microservices at your service](https://www.lingsoft.fi/en/microservices-at-your-service-bridging-gap-between-nlp-research-and-industry).

# European Language Grid
The docker image is hosted [here](https://hub.docker.com/r/glaciersg/tokenizer_api) and is running on the european language grid as [icelandic tokenizer](https://live.european-language-grid.eu/catalogue/tool-service/17480).
