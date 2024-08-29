import requests
from bs4 import BeautifulSoup
from typing import List

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text
# print(yc_webpage)

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.title)

# get all the news titles in the hacker news website
articles: List[str] = soup.find_all(name='a', class_='storylink')

articule_texts: List[str] = []
articule_links: List[str] = []
for article in articles:
    articule_texts.append(article.getText())
    articule_links.append(article.get('href'))

articule_upvotes: List[str] = []
for score in soup.find_all(name='span', class_='score'):
    articule_upvotes.append(int(score.getText().split()[0]))

print(articule_texts)
print(articule_links)
print(articule_upvotes)

# find out the title and link for the story with the highest number of upvotes.
max_upvotes: int = max(articule_upvotes)
article_title_with_highest_upvotes: str = articule_texts[articule_upvotes.index(max_upvotes)]
artitle_link_with_highest_upvotes: str = articule_links[articule_upvotes.index(max_upvotes)]
print(article_title_with_highest_upvotes)
print(artitle_link_with_highest_upvotes)
