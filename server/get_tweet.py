import lib
def pull_info(tweet):
    data = {
        'content': tweet['full_text']
    }
    return data

params = {
    'q': 'telsa',
    'tweet_mode': 'extended',
    'lang': 'en',
    'count': '100'
}

response = requests.get(
    'https://api.twitter.com/1.1/search/tweets.json',
    params=params,
    headers={'authorization': 'Bearer '+'AAAAAAAAAAAAAAAAAAAAAK%2FuagEAAAAAZNY2%2BHt7vL013A49S3sxYK4XJJA%3Dwodzkz6BJvrScFBOyPufuSABYiM0cY4aPO5Gmu6mlDrjzPqIZg'}
    )

