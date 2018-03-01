

```python
# Dependencies & base url
import requests
import json
from pprint import pprint
from mydata import NYT_API_key
import time

base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
```


```python
# define term used to search
query = "Xi+Jinping"
```


```python
# define time limit for search
begin = "&begin_date=20180101"
end = "&end_date=20180301"
```


```python
# define api key
key = "api-key=" + NYT_API_key
```


```python
# Build query URL
url = base_url + key + begin + end + "&q=" + query + "&sort=newest"
```


```python
# Request 30 articles at one time
article_list = []
for i in range(3):
    time.sleep(1)  
    new_url = url + "&page=" + str(i)
    articles = requests.get(new_url).json()
    for item in articles["response"]["docs"]:        
        article_list.append(item)
```


```python
# print info (publish date, time, source, author & snippet)
for i in range(len(article_list)):
    print(str(i+1) + ". Published on: " + article_list[i]['pub_date'])
    print("Source: " + article_list[i]['source'])
    if article_list[i]['byline']['person'] == []:
        print("Author: unknown")
    elif article_list[i]['byline']['person'] == None:
        print("Author: unknown")
    else:       
        print("Author: " + article_list[i]['byline']['person'][0]['firstname']
             + ' ' + article_list[i]['byline']['person'][0]['lastname'])
    print(article_list[i]['snippet'])
    print('--------------------------')
```

    1. Published on: 2018-02-28T23:48:44+0000
    Source: The New York Times
    Author: Damien CAVE
    This week’s Australia Letter highlights coverage and events exploring the state of democracy and gender. Plus, stories that make us smile.
    --------------------------
    2. Published on: 2018-02-28T19:15:37+0000
    Source: Reuters
    Author: unknown
    Top aides to President Donald Trump look to push a tough line on trade in talks on Thursday with an envoy of Chinese President Xi Jinping, with a White House official saying a frank exchange of views was expected.
    --------------------------
    3. Published on: 2018-02-28T19:02:05+0000
    Source: The New York Times
    Author: Inyoung KANG
    Here’s what you need to know to start your day.
    --------------------------
    4. Published on: 2018-02-28T12:20:21+0000
    Source: The New York Times
    Author: unknown
    Spotify has revived the fortunes of recording artists, funneling billions of dollars to music companies. But a charity Spotify is not.
    --------------------------
    5. Published on: 2018-02-28T10:01:07+0000
    Source: The New York Times
    Author: Max FISHER
    China kept a half-century of global democratic growth at bay by at least nodding to the importance of institutions and rules. Now what?
    --------------------------
    6. Published on: 2018-02-28T09:54:37+0000
    Source: Reuters
    Author: unknown
    A vice minister of public security, a close confidant of President Xi Jinping, is tipped to take over as China's spy master, five sources said, as the country looks to clean up its security apparatus and plug intelligence gaps.
    --------------------------
    7. Published on: 2018-02-28T09:39:45+0000
    Source: Reuters
    Author: unknown
    China is developing technologies to build a nuclear-powered aircraft carrier, state media reported on Wednesday, as Beijing pushes forward with an ambitious military modernisation programme.
    --------------------------
    8. Published on: 2018-02-28T09:33:55+0000
    Source: Reuters
    Author: unknown
    China is developing technologies to build a nuclear-powered aircraft carrier, state media reported on Wednesday, as Beijing pushes forward with an ambitious military modernization program.
    --------------------------
    9. Published on: 2018-02-28T08:51:36+0000
    Source: Reuters
    Author: unknown
    Reforms to China's constitution to remove term limits for the presidency does not mean life-long terms, the ruling Communist Party's official People's Daily said on Thursday, after a surge of concern that Xi Jinping may stay in power forever.
    --------------------------
    10. Published on: 2018-02-28T06:06:38+0000
    Source: Reuters
    Author: unknown
    With stealth jets entering service, leaked pictures of new high-tech naval artillery and proud reports of manoeuvres that "dare to shine the sword," China's armed forces are putting on a show of power as they lobby for greater defence spending.
    --------------------------
    11. Published on: 2018-02-28T05:01:20+0000
    Source: The New York Times
    Author: Patrick BOEHLER
    Here’s what you need to know to start your day.
    --------------------------
    12. Published on: 2018-02-28T01:40:09+0000
    Source: The New York Times
    Author: Mark LANDLER
    Whether it is saber-rattling in the South China Sea, proselytizing on American campuses or censorship of the web, China has alienated one constituency after another.
    --------------------------
    13. Published on: 2018-02-27T23:55:14+0000
    Source: The New York Times
    Author: Thomas FRIEDMAN
    Strongmen know not to worry that America will stand up to them.
    --------------------------
    14. Published on: 2018-02-27T23:12:52+0000
    Source: The New York Times
    Author: Karen ZRAICK
    Here’s what you need to know at the end of the day.
    --------------------------
    15. Published on: 2018-02-27T22:12:44+0000
    Source: Reuters
    Author: unknown
    Three of President Donald Trump's senior economic aides are expected to meet this week with a top Chinese economic official to discuss trade disputes between the United States and China.
    --------------------------
    16. Published on: 2018-02-27T20:36:31+0000
    Source: The New York Times
    Author: unknown
    Decades of hope that China might join a global liberal order are dashed. He can be president for life, as China becomes more dominant in the world.
    --------------------------
    17. Published on: 2018-02-27T19:03:32+0000
    Source: The New York Times
    Author: Inyoung KANG
    Here’s what you need to know to start your day.
    --------------------------
    18. Published on: 2018-02-27T18:30:12+0000
    Source: The New York Times
    Author: Jane PERLEZ
    The Chinese leader has new authority to pursue his drive to make China a dominant global power — even if it risks putting Beijing in conflict with Washington.
    --------------------------
    19. Published on: 2018-02-27T16:28:10+0000
    Source: The New York Times
    Author: Patrick CHAPPATTE
    China’s Communist Party announced Sunday that it intends to abolish limits on presidential terms.
    --------------------------
    20. Published on: 2018-02-27T12:20:43+0000
    Source: The New York Times
    Author: unknown
    Fox can either revise the terms of the Disney sale to exclude Sky, or enter into a bidding war with Comcast. Neither option is appealing.
    --------------------------
    21. Published on: 2018-02-27T10:42:36+0000
    Source: AP
    Author: unknown
    A Chinese anti-graft official on Tuesday said a new regulation allowing the detention of corruption suspects for up to six months without charge is "based on rule of law."
    --------------------------
    22. Published on: 2018-02-27T10:30:10+0000
    Source: The New York Times
    Author: Chris STANFORD
    Here’s what you need to know to start your day.
    --------------------------
    23. Published on: 2018-02-27T09:21:44+0000
    Source: AP
    Author: unknown
    The ruling Communist Party's move to let leader Xi Jinping remain China's president indefinitely is fueling anxiety that Beijing might be undermining reforms needed to keep its economy healthy.
    --------------------------
    24. Published on: 2018-02-27T07:06:37+0000
    Source: Reuters
    Author: unknown
    China on Tuesday defended a controversial detention measure set to become law when a new anti-corruption "super-ministry" is formally set up next month, calling it a unique step necessary to combat graft.
    --------------------------
    25. Published on: 2018-02-27T05:45:43+0000
    Source: Reuters
    Author: unknown
    China is expected to announce a reshuffle of its top diplomats at an annual meeting of parliament in March, aiming to deal with U.S. President Donald Trump's growing suspicion of Beijing, several sources familiar with the plan said.
    --------------------------
    26. Published on: 2018-02-27T05:40:04+0000
    Source: AP
    Author: unknown
    In a rare public expression of dissent in China, a well-known political commentator and a prominent businesswoman have penned open letters urging lawmakers to reject a plan that would allow President Xi Jinping to rule indefinitely.
    --------------------------
    27. Published on: 2018-02-27T05:06:22+0000
    Source: The New York Times
    Author: Patrick BOEHLER
    Here’s what you need to know to start your day.
    --------------------------
    28. Published on: 2018-02-27T04:33:45+0000
    Source: Reuters
    Author: unknown
    Zhou Xiaochuan, China's longest-serving central bank governor, is tipped to become the new vice chairman of the Boao Forum -- known as Asia's Davos -- after he retires next month, sources said. 
    --------------------------
    29. Published on: 2018-02-26T23:08:20+0000
    Source: The New York Times
    Author: Zach JOHNK
    Here’s what you need to know at the end of the day.
    --------------------------
    30. Published on: 2018-02-26T19:02:45+0000
    Source: The New York Times
    Author: Penn BULLOCK
    Here’s what you need to know to start your day.
    --------------------------



```python
# Print the web_url of each stored article
print("Your Reading List")
for article in article_list:
    print(article["web_url"])
```

    Your Reading List
    https://www.nytimes.com/2018/02/28/world/australia/democracy-adelaide-festival-gender-letter47.html
    https://www.nytimes.com/reuters/2018/02/28/business/28reuters-usa-china-trade.html
    https://www.nytimes.com/2018/02/28/briefing/xi-jinping-jared-kushner-brexit.html
    https://www.nytimes.com/2018/02/28/business/dealbook/dicks-guns.html
    https://www.nytimes.com/2018/02/28/world/asia/xi-jinping-china.html
    https://www.nytimes.com/reuters/2018/02/28/world/asia/28reuters-china-politics-security-exclusive.html
    https://www.nytimes.com/reuters/2018/02/28/world/asia/28reuters-china-defence-aircraft.html
    https://www.nytimes.com/reuters/2018/02/28/world/asia/28reuters-china-defence-nuke.html
    https://www.nytimes.com/reuters/2018/02/28/world/asia/28reuters-china-politics.html
    https://www.nytimes.com/reuters/2018/02/28/world/asia/28reuters-china-defence.html
    https://www.nytimes.com/2018/02/28/briefing/diesel-italy-election-kushner.html
    https://www.nytimes.com/2018/02/27/us/politics/trump-china-united-states.html
    https://www.nytimes.com/2018/02/27/opinion/trump-strongmen-democracy.html
    https://www.nytimes.com/2018/02/27/briefing/jared-kushner-nra-syria.html
    https://www.nytimes.com/reuters/2018/02/27/business/27reuters-usa-trump-china.html
    https://www.nytimes.com/2018/02/27/opinion/xi-jinping-power-china.html
    https://www.nytimes.com/2018/02/27/briefing/syria-global-warming-taiwan.html
    https://www.nytimes.com/2018/02/27/world/asia/xi-jinping-china-new-cold-war.html
    https://www.nytimes.com/2018/02/27/opinion/xi-jinping-power-grab.html
    https://www.nytimes.com/2018/02/27/business/dealbook/comcast-fox-sky.html
    https://www.nytimes.com/aponline/2018/02/27/world/asia/ap-as-china-corruption-detention.html
    https://www.nytimes.com/2018/02/27/briefing/florida-comcast-delta-air-lines.html
    https://www.nytimes.com/aponline/2018/02/27/world/asia/ap-as-china-politics-business.html
    https://www.nytimes.com/reuters/2018/02/27/world/asia/27reuters-china-politics-corruption.html
    https://www.nytimes.com/reuters/2018/02/27/world/asia/27reuters-china-diplomacy.html
    https://www.nytimes.com/aponline/2018/02/27/world/asia/ap-as-china-politics.html
    https://www.nytimes.com/2018/02/27/briefing/angela-merkel-china-syria.html
    https://www.nytimes.com/reuters/2018/02/26/business/26reuters-china-economy-pboc-zhou.html
    https://www.nytimes.com/2018/02/26/briefing/trump-daca-roger-goodell.html
    https://www.nytimes.com/2018/02/26/briefing/xi-jinping-syria-boko-haram.html

