import os
from dotenv import load_dotenv
import tweepy
import sys
from datetime import date
import json

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

# set day accoding to date
DAY_FILE="day_data.json"
def load_day():
   current_date=date.today()

   #if ran for first time
   if not os.path.isfile(DAY_FILE):
    data={"day":1,"last_posted":current_date.isoformat()}
    with open(DAY_FILE,"w") as my_file:
        json.dump(data,my_file)
    return 1
   
   #if ran previously than add day
   with open(DAY_FILE,"r") as my_file:
      data=json.load(my_file)
      last_date=date.fromisoformat(data["last_posted"])
    
   days_passed=(current_date-last_date).days

   if (days_passed > 0):
       day_today=data["day"]+days_passed
       data={"day":day_today,"last_posted":current_date.isoformat()}
       with open(DAY_FILE,"w") as my_file:
           json.dump(data,my_file)

   return(day_today)

if __name__ == "__main__":
    day = load_day()

    if len(sys.argv) > 1:
        image_path=sys.argv[1]
        print(f"Provided file path is: {image_path}")
    else:
        print("Please provide a file path as a command-line argument.")
        sys.exit(1)
    tags_to_mention = ["geeksforgeeks"]

    # post_tweet(day, image_path, tags_to_mention)