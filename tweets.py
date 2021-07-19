import tweepy
import config


#필요한 설정값 가져오기
api_key = config.api_key
api_secret = config.api_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

#핸들러 생성 및 개인정보 인증
auth = tweepy.OAuthHandler(api_key, api_secret)

#액세스 요청
auth.set_access_token(access_token, access_token_secret)

#tweepy.API 생성
api = tweepy.API(auth)



def get_tweets(screen_name):
	tweets = []
	stuff = api.user_timeline(screen_name = screen_name, count = 100, include_rts = False, tweet_mode='extended')

	for status in stuff:
		tweets.append(status.full_text)

	return tweets

