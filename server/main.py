from code import compile_command
from concurrent.futures import process
import get_tweet as tweet
import match_name as translate
import queue_up as myQueue
import sentiment_check as senCheck
import symbol_check as symCheck
import lib_import as lib


def main(userInput):
    


    processedInput = symCheck.inputProcess(userInput)

    
    companyName = translate.match()

    companyList =[]
    for company in processedInput:
        companyList.append(translate.get_name(company, companyName))
    
    #print(companyList)
    companyScore = []
    sentiment_model = lib.flair.models.TextClassifier.load('en-sentiment')
    for company in processedInput:
        print('Processing...' + company)
        df = lib.pd.DataFrame(tweet.get_tweet(company))
        companyScore.append(senCheck.sen_check(df,sentiment_model))
       
    print("Companies: ")
    print(processedInput)
    print("Sentimental score: ")
    print(companyScore)
    companyScoreDict = dict(zip(processedInput, companyScore))

    queue = myQueue.queue_up(processedInput,companyScoreDict)
    print("Top 3 Recommendation: ") 

    return queue

userInput = ['TsLA','NvdA','AMD','GOOGl','AmZn']
queue = main(userInput)

print(queue)
