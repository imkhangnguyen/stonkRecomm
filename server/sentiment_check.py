import get_tweet as tweet

sentiment_model = tweet.flair.models.TextClassifier.load('en-sentiment')

sentimental_score = 0
for tweet in tweet.df['content']:
    #Setting clean up parameters
    whitespace = tweet.re.compile(r"\s+")
    web_address = tweet.re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
    tesla = tweet.re.compile(r"(?i)@Tesla(?=\b)")
    user = tweet.re.compile(r"(?i)@[a-z0-9_]+")
    
    #Cleaning up tweet
    tweet = whitespace.sub(' ', tweet)
    tweet = web_address.sub('', tweet)
    tweet = tesla.sub('Tesla', tweet)
    tweet = user.sub('', tweet)
    sentence = tweet.flair.data.Sentence(tweet)
    sentiment_model.predict(sentence)
    
    #Get sentimental score
    sentiment = sentence.labels[0].value
    if sentiment == 'POSITIVE':
        sentimental_score = sentimental_score + 1
    else:
        sentimental_score = sentimental_score - 1
        
