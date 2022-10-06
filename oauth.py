import tweepy

api_key = "ON1rxELa7QBheuzNjKrk5kZEl"
api_secrets = "9YWhD8HUaFvhHncdYRJLsJ5RQK5hPC2M6ip4L2tAgaeFXgNCrY"
access_token = "1447875549880217602-IHSHK0tipxsWWRQkU98UDELEEYwzY2"
access_secret = "BrwUMsj5kACeCx9WjvOIYuGwSOLpzfX63CW8nfpdznLRN"
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)
print(api)
