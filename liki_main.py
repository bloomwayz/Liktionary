import requests
from bs4 import BeautifulSoup as bs
from random import *
import pandas as pd

targetUrl = 'https://raw.githubusercontent.com/BlossomWay/Liktionary/main/liki_corpus.csv'
df = pd.read_csv(targetUrl)
words = df.values.tolist()

index = randint(1, 3315)
print(index)

page = requests.get("https://en.wiktionary.org/wiki/" + words[index][0])
soup = bs(page.text, "html.parser")

elements = soup.select('#mw-normal-catlinks > ul > li')
for element in elements:
	print(element.text)

def idk(i):
    buffer = input('Trial ' +  str(i) + ' or Surrender(if you input \"surrender\"):\n')

    if buffer == words[index][0]:
        print('Congratulations!\nYou got it in ' + str(i) + ' times.')
    elif buffer == "surrender":
        print('I\'m sorry to hear that. The answer is \"' + words[index][0] + '\".')
    else:
        i = i+1
        idk(i)

idk(1)
