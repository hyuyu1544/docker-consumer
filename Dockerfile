FROM python:3.7.4-alpine
WORKDIR /docker_consumer
COPY . /docker_consumer
RUN pip install -r requirements.txt
ENV TZ=Asia/Taipei
CMD ["python", "consumer.py"]