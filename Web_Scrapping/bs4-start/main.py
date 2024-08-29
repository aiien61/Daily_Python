# import lxml
from bs4 import BeautifulSoup
from typing import List

with open('website.html', 'r') as webpage:
    content = webpage.read()
# print(content)

soup = BeautifulSoup(content, 'html.parser')
print(soup.title) # include tag and the text of the tag
print(soup.title.name) # the name of the tag
print(soup.title.string) # the text in between opening and closing tags

# get the first item of the particular tag
print(soup.a)
print(soup.p)
print(soup.li)

# get the all items of the particular tag
all_anchor_tags: List[str] = soup.find_all(name='a')
print(all_anchor_tags)

# get the text of the tag
for tag in all_anchor_tags:
    print(tag.getText())

# get the link of the anchor tag
for tag in all_anchor_tags:
    print(tag.get('href'))


# get the particular item when specifying multiple elements
heading: str = soup.find(name='h1', id='name')
print(heading)

section_heading: str = soup.find(name='h3', class_='heading')
print(section_heading)
print(section_heading.name)
print(section_heading.getText())

# get the item using CSS selector when sandwiched in nested tags
company_url: str = soup.select_one(selector='p a')  
print(company_url)

name: str = soup.select_one(selector='#name')
print(name)

headings: List[str] = soup.select('.heading')
print(headings)