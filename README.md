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
docker-compose up -d --build
```

Then the consumer begining, you can see log in container like this:
```
INFO:[YYYY-mm-dd HH:MM:SS]: start consumer...
```

### The problem you may facing...

1. rabbitMQ connection fail.
```
pika.exceptions.ConnectionClosed: Connection to 127.0.0.1:5672 failed: [Errno 111] Connection refused
```

solution 1: recheck your rabbitMQ container's port is open

solution 2: use `ifconfig` to get IP and change `RABBITMQ_HOST` which in `docker-compose .yml`
