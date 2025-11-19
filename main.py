import os
import random
import requests
import tweepy


def get_random_media():
    path = 'assets' 
    objects = os.listdir(path)

    media = random.choice(objects)
    return os.path.join(path, media)


def auth_v1(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret):
    return tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret,
        return_type=requests.Response,
    )


def tweet(media) -> requests.Response:
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    api_v1 = auth_v1(consumer_key, consumer_secret,
                     access_token, access_token_secret)
    client_v2 = auth_v2(consumer_key, consumer_secret,
                        access_token, access_token_secret)

    media_id = api_v1.media_upload(media).media_id

    return client_v2.create_tweet(media_ids=[media_id])


def main():
    medias = get_random_media()
    tweet(medias)


if __name__ == '__main__':
    main()
