# import libraries
import auth_tokens as auth
import tweepy
import logging
import json
import time

from confluent_kafka import Producer

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

search_term = 'covid19'

# Login with twitter auth v1.1
def loginV1(auth):
    authentication = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
    authentication.set_access_token(auth.access_token, auth.access_secret) #v1.1
    client = tweepy.API(authentication)
    return client

# Login with twitter auth v2
def loginV2(auth, search_term):
    client = tweepy.Client(auth.bearer_token)
    tweets = client.search_recent_tweets(query=search_term, max_results=100)
    return tweets

p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    for tweet in tweets.data:
        data={
           'id': tweet.id,
           'text':tweet.text
           }
        m=json.dumps(data)
        p.poll(1)
        p.produce('covid-topic', m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(3)

if __name__ == '__main__':
    tweets = loginV2(auth, search_term)
    main()