import os
from dotenv import load_dotenv
import tweepy
import sys

load_dotenv()

# Tweepy OAuth1 for v1.1 media upload
auth = tweepy.OAuth1UserHandler(
    os.getenv("CONSUMER_KEY"),
    os.getenv("CONSUMER_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)

# Tweepy Client for v2 tweeting
client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

#get url of the post
def get_url(text):
    index=text.find("https:")
    return (text[index:])

#upload image using v1.1 and get id
def upload_image(image_path):
    media = api.media_upload(image_path)
    return media.media_id_string

def post_tweet(day_count, image_path, tags_list):
    hashtags = "#gfg160 #geekstreak2025"
    tags = " ".join([f"@{tag}" for tag in tags_list])
    text = f"Day {day_count} today! {hashtags} {tags} tweet bot testing"

    media_id = upload_image(image_path)

    # posting tweet using v2 and combing with image uploaded
    response = client.create_tweet(text=text, media_ids=[media_id])
    url=get_url(response.data['text'])
    print(f"Tweet posted! ID: {response.data['id']}\nView Tweet: {url}")

if __name__ == "__main__":
    day = 41

    if len(sys.argv) > 1:
        image_path=sys.argv[1]
        print(f"Provided file path is: {image_path}")
    else:
        print("Please provide a file path as a command-line argument.")
        sys.exit(1)
    tags_to_mention = ["geeksforgeeks"]

    post_tweet(day, image_path, tags_to_mention)