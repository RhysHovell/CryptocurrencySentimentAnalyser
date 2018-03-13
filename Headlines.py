
import requests
import json
import time


from nltk.sentiment.vader import SentimentIntensityAnalyzer as SA


hdr = {'User-Agent': 'windows:r/CryptoCurrency.single.result:v1.0' + '(by /u/Tulkas2386)'}
url = 'https://www.reddit.com/r/CryptoCurrency/.json'
req = requests.get(url, headers=hdr)
json_data = json.loads(req.text)

dataAll = json_data['data']['children']
num_posts = 0
while len(dataAll) <= 1000:
    time.sleep(2)
    last = dataAll[-1]['data']['name']
    url = 'https://www.reddit.com/r/CryptoCurrency/.json?after='+str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    dataAll += data['data']['children']
    if num_posts == len(dataAll):
        break
    else:
        num_posts = len(dataAll)


SA = SA()
positiveList = []
negativeList = []

for post in dataAll:
    results = SA.polarity_scores(post['data']['title'])
    if results['compound'] > 0.2:
        positiveList.append(post['data']['title'])
    elif results['compound'] <-0.2:
        negativeList.append(post['data']['title'])

with open("positiveNews.txt", "w" , encoding='utf-8', errors='ignore') as positive:
    for post in positiveList:
        positive.write(post+"\n")

with open("negativeNews.txt", "w" , encoding='utf-8', errors='ignore') as negative:
    for post in negativeList:
        negative.write(post+"\n")



