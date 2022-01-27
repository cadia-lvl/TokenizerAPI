docker stop tokenizer
docker container rm tokenizer
docker build . -t glaciersg/tokenizer_api:latest
docker run -d -p 8080:8080 --name=tokenizer glaciersg/tokenizer_api:latest
