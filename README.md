# docker-consumer: consumer only

資料進入rabbitmq後，經過consumer對資料預處理，再送進欲儲存的資料庫（以elasticsearch為例）。

### Execution

Build elasticsearch DB and rabbitMQ first:
```
docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:management
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.1
```

Clone the registry and build the docker image:
```
git clone https://github.com/hyuyu1544/docker-consumer.git
cd docker-consumer/
docker build -f Dockerfile -t consumer:latest . --no-cache
```

You can add your own registry before the image name, then you can `push` to your dockerhub: `docker push <your_registry>/consumer:<version>`
Then next time, just `docker-compose up -d --build` can pull the image from your dockerhub.


```
docker-compose up -d --build
```
