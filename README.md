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

In the test folder, basic scripts for testing the functionality of the API can be found .

## Testing ELG

For testing if the [ELG specifications](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern) are being met, you must specify which API you want to test in the `.env` file. Then you run `docker-compose up` and submit the API calls to `localhost:8080/process/service`.

# Funding
This ELG API was developed by the [Language and Voice Lab](https://lvl.ru.is/) at [Reykjavík University](https://en.ru.is/) in EU's CEF project: [Microservices at your service](https://www.lingsoft.fi/en/microservices-at-your-service-bridging-gap-between-nlp-research-and-industry).

# European Language Grid
The docker image is hosted [here](https://hub.docker.com/r/glaciersg/tokenizer_api) and is running on the European Language grid as [
ELG API for Icelandic Tokenizer](https://live.european-language-grid.eu/catalogue/tool-service/17480).

# Underlying tool
The underlying tokenizer is [Tokenizer](https://github.com/mideind/Tokenizer) by [Miðeind](https://mideind.is/), which is licensed under this [MIT license](https://github.com/mideind/Tokenizer/blob/master/LICENSE).  The ELG API implementation imports the corresponding [PyPi package](https://pypi.org/project/tokenizer/).

