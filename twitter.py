import tweepy
import csv 
import random
from datetime import date, timedelta

auth = tweepy.auth.OAuthHandler('K4LmAWkBZQ226KXrhTR12QyCg', 'TmiMBOeaeNO3rgi2NabDQzLrVFjXOlXy8T7rxZqQvQTBHN6tYA')
auth.set_access_token('1120336191113457664-jryhny1g8yplK0BvwB918KdIRW4jn2', 'PdNUONExvxYwqHxHAQm0U1gqverAIOBoi4f0LZMvNaOLT')

api = tweepy.API(auth)


randNumber = random.randint(0,9999)
fileName = 'tweetInfo'+str(randNumber)+'.csv'
csvFile = open(fileName, 'a', encoding="utf-8")

day = date.today() - timedelta(hours=24)

csvWriter = csv.writer(csvFile)

i = 0
for tweet in tweepy.Cursor(api.search,q="#Twitter",
                        lang="en",
                        since=day).items():
    if i < 100:
        print("Extracting tweet ",i)
        csvWriter.writerow([tweet.created_at, tweet.text,tweet.source, tweet.user.name, tweet.user.location, tweet,id, tweet.user.profile_image_url_https, tweet.user.profile_sidebar_fill_color])
        i = i+1
    else :
        print("\nExtraction of live data complete\n")
        break

csvFile.close()