# kafka-producer-twitter

This is repository for streaming API twitter data using Apache Kafka. In this case I'll be using twitter data with search topic as `Covid19`.

Pre-requisite:
1. Python 3.7 or later. Please note that `confluent_kafka` will resulting error in `python 3.8.8` based on this [link](https://github.com/confluentinc/confluent-kafka-python/issues/1186) 
2. Kafka confluent. Install with command `pip install confluent_kafka`.
3. Tweepy. Install with command `pip install tweepy`.

How to run:
1. Open docker and start running `docker-compose.yml` file with command `docker-compose up`.
2. Fill in your twitter API credentials in `auth_tokens.py` file with your own. You can get that [here](developer.twitter.com).
3. Run file `kafkaProducer.py`. Note: Edit the file for V1 login if you want to use V1 Auth in twitter.
4. Open another terminal and run file `kafkaConsumer.py` to see the streamed data from kafka.
