import cohere
from cohere.classify import Example
from newsapi import NewsApiClient
from random import randint

co = cohere.Client('KNiwDymfXTQHSRC5QQUlzUvun5H36n6hOS7cZQod')

def newsOptimism(articleTitle):
    classifications = co.classify(
    inputs=[articleTitle],
    examples=[Example("Hack the North\'s opening message: \'Be audacious\'Musician will.i.am tells Waterloo hackathon students to think big and collaborate across disciplines", "positive"), Example("Monkeypox vaccine available to more New Brunswickers", "positive"), Example("Feds announce $38K to help equity-deserving kids pay for sports, dance programs in Waterloo Region", "positive"), Example("Scientists are using AI to dream up revolutionary new proteins", "positive"), Example("Morning house fire in Estaire", "negative"), Example("One dead in triple stabbing near St. Laurent Shopping Centre", "negative"), Example("Russia-Ukraine: EU calls for war crime court over mass grave", "negative"), Example("Canadian households have lost billions in real estate cool-down", "negative"), Example("Threats made against 2SLGBTQ+ group at Edmonton’s Pride Corner", "negative"), Example("Ig Nobel prizes 2022: The unlikely science that won this year\'s awards", "Neutral"), Example("UN warns 345 million people face starvation worldwide", "negative"), Example("Saturn\'s rings and tilt might have come from one missing moon", "Neutral"), Example("19-year-old fatally shot", "negative"), Example("The world\'s second biggest cryptocurrency just got a lot greener", "positive"), Example("Barcelona 3-0 Elche: Robert Lewandowski scores twice as Xavi\'s side move top of La Liga", "Neutral"), Example("Meet \'ROLL-E,\' Surrey\'s first Urban Technology Test Lab pilot", "Neutral"), Example("Eating insects can be good for the planet – Europeans should eat more of them", "positive"), Example("Why defusing ‘carbon bombs’ offers a promising new agenda for tackling climate change", "positive"), Example("Oak Park High School opens Indigenous outdoor classroom", "Neutral"), Example("$50-million gift to create ‘leadership’ college at McMaster University", "positive")])

    confidence = classifications.classifications[0].labels['positive'].confidence
    if(confidence > 0.5):
        return "positive"
    else:
        return "negative"
newsapi = NewsApiClient(api_key='bc0d2ad934b346f08d2d50f0ad90c81f')
articleInfoList = newsapi.get_top_headlines()["articles"]
manualArticles = [{'title':'''Hack the North's opening message: Be audacious''','link':'''https://communitech.ca/technews/hack-the-norths-opening-message-be-audacious.html'''},{'title':'Burial site with 445 bodies outside Izyum shows evidence of war crimes, Ukraine says','link':'https://www.theglobeandmail.com/world/article-mass-burial-site-outside-izyum-shows-evidence-of-war-crimes-ukraine/'},{'title':'Province Recognizes Group of Seniors at Awards Ceremony',
'link':'https://vocm.com/2022/09/17/province-recognizes-group-of-seniors-at-awards-ceremony/'}, {'title':''''''}, {'title':'''Toronto film festival 2022 roundup - Spielberg, Mendes and a deep, joyous love of cinema''',
'link':'https://www.theguardian.com/film/2022/sep/17/toronto-film-festival-2022-review-the-fabelmans-spielberg-empire-of-light-mendes-the-good-nurse-eddie-redmayne-the-woman-king-viola-davis-glass-onion-daniel-craig-the-menu-mark-mylod'},{'title':'Monkeypox vaccine available to more New Brunswickers',
'link':'https://www.cbc.ca/news/canada/new-brunswick/monkeypox-vaccine-new-brunswick-expanded-availability-pre-exposure-1.6585371'},{'title':'Scientists are using AI to dream up revolutionary new proteins','link':'https://www.nature.com/articles/d41586-022-02947-7'},{'title':'''Meet 'ROLL-E,'Surrey's first Urban Technology Test Lab pilot''','link':'https://www.surrey.ca/news-events/news/meet-roll-e-surreys-first-urban-technology-test-lab-pilot-project'},{'title':'''Ethereum, The World's Second Biggest Cryptocurrency Just got a lot Greener''','link':'https://www.cbc.ca/radio/day6/ethereum-cryptocurrency-gone-green-1.6584135'},{'title':'Saturn\'s rings and tilt might have come from one missing moon',
'link':'''https://www.sciencenews.org/article/destroyed-moon-chrysalis-caused-saturns rings#:~:text=This%20hypothetical%20missing%20moon%2C%20dubbed,that%20encircle%20the%20planet%20today.'''}]
def getNewsArticle():
    randomArticleNum = randint(0,24)
    if randomArticleNum <= 19:
        newsArticle = articleInfoList[randomArticleNum]["title"]
        articleLink = articleInfoList[randomArticleNum]["url"]
    else:
        newsArticle = manualArticles[randomArticleNum-20]['title']
        articleLink = manualArticles[randomArticleNum-20]['link']

    #print(newsapi.get_top_headlines())
    return {'title': newsArticle, 'link': articleLink}

newsRating = input("Do you want positive or negative news? ")
articleAmouont = 3

articleList = []

while True:
    article = getNewsArticle()
    title = article['title']
    url = article['link']

    if newsOptimism(title) == newsRating and title not in articleList:
        articleList.append(title)
        print("article:", title)
        print("url:", url)
        print('\n')
    if len(articleList) >= articleAmouont:
        break
# print(articleList)
# for x in range (0,40):
# print(getNewsArticle())
