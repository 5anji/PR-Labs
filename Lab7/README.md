# Steps to run

## Setup enviroment

```bash
python -m venv venv
source ./venv/bin/activate
pip install beautifulsoup4 requests pika tinydb
```

## Launch rabbitmq (Docker)

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
```

## Fill queue

```bash
python3 producer.py
```

## Process queue and export to db

```bash
python3 consumer.py
```
