
import requests
import json
import time


def headlines():
    from nltk.sentiment import SentimentIntensityAnalyzer as SA

    SA = SA()

    posCompound = 0.2
    negCompound = -0.2
    numHeadlines = 1000

    positiveList = []
    negativeList = []
    hdr = {'User-Agent': 'windows:r/CryptoCurrency.single.result:v1.0' + '(by /u/Tulkas2386)'}
    url = 'https://www.reddit.com/r/CryptoCurrency/.json'
    req = requests.get(url, headers=hdr)
    jsonData = json.loads(req.text)

    dataAll = jsonData['data']['children']
    numPosts = 0
    while len(dataAll) <= numHeadlines:
        time.sleep(2)
        last = dataAll[-1]['data']['name']
        url = 'https://www.reddit.com/r/CryptoCurrency/.json?after=' + str(last)
        req = requests.get(url, headers=hdr)
        data = json.loads(req.text)
        dataAll += data['data']['children']
        if numPosts == len(dataAll):
            break
        else:
            numPosts = len(dataAll)


    for post in dataAll:
        results = SA.polarity_scores(post['data']['title'])
        if results['compound'] > posCompound:
            positiveList.append(post['data']['title'])
        elif results['compound'] < negCompound:
            negativeList.append(post['data']['title'])

    with open("Data/positiveNews.txt", "w", encoding='utf-8', errors='ignore') as positive:
        for post in positiveList:
            positive.write(post + "\n")

    with open("Data/negativeNews.txt", "w", encoding='utf-8', errors='ignore') as negative:
        for post in negativeList:
            negative.write(post + "\n")

    return positiveList, negativeList


def statusHeadline():

    status = "Started"
    return status
