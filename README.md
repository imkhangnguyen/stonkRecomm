# stonkRecomm
A simple web-app that allows the users to enter a list of stocks and output top 3 stocks based on the public sentiment. 


Problem: There are too many stocks in the market which can confuse newcomers. Users may
not have time to research their stock picks adequately or to get a good idea of public perception
of the stocks they want to buy.


Solution: A web-application to help the users to choose out the best stocks based on their own
list of stocks.


Description: Users can enter symbols for which stocks they are interested in and the app will use
the Twitter API to return a list of tweets for each stock. The app will then use the Flair NLP
framework to determine whether the sentiment of each tweet is positive or negative. The sum of
the sentiment values of each of the most relevant tweets will be the recom mendation key for
each stock. Each stock and its key will be stored in a dictionary. All of the stocks will be added
to a priority queue. The program will remove the highest priority stock element from the queue
and provide it to the user. This allows the user to select the stock with the best overall sentiment
from their watchlist in order to make the best purchase.
