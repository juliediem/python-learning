import requests
from bs4 import BeautifulSoup
import requests
import regex as re

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titleline = soup.find_all(class_="titleline")

article_link = []
article_text = []
for title in titleline:
    anchor = title.find("a")
    anchor_link = anchor.get("href")
    article_link.append(anchor_link)
    article_title = anchor.getText()
    article_text.append(article_title)

print(article_link)
print(article_text)

# Using regex to find
# subline = soup.find_all(id=re.compile(r'^score_'))

upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name="span", class_="score")]

print(upvotes)

# highest_score=0
# for upvote in upvotes:
#     if upvote > highest_score:
#         highest_score=upvote

highest_score = max(upvotes)

highest_score_index = upvotes.index(highest_score)
print(highest_score_index)

print(article_text[highest_score_index])
print(article_link[highest_score_index])
print(upvotes[highest_score_index])

# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
#
# # Option 1: Use CSS Selectors like selector="p a". so you're looking for something sitting inside an a href tag, and a paragraph tag.
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
# # Option 2: Use id Selector, by using # sign
# name = soup.select_one(selector="#name")
# print(name)
# # Option 3: Select based on class, use the dot notation
# headings = soup.select(".heading")
# print(headings)
#
