docker stop tokenizer
docker container rm tokenizer
docker build . -t tokenizer:v1
docker run -d -p 8080:8080 --name=tokenizer tokenizer:v1
