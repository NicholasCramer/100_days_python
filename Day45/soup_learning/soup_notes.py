from bs4 import BeautifulSoup
import requests

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="ul a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)


# scraping from live url

url = "https://news.ycombinator.com/news"
response = requests.get(url)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

news = soup.find_all(class_="titleline")

article_texts= []
article_links = []
article_upvotes = []
for article_tag in news:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_scores = soup.find_all(name="span", class_="score")
for score in article_scores:
    upvotes = int(score.getText().split()[0])
    article_upvotes.append(upvotes)

# first_article_link = news[0].find(name="a").get("href")
# first_article_text = news[0].find(name="a").getText()
# first_article_score = article_scores[0].find(class_="score").getText()
# print(first_article_link)
# print(first_article_text)
# print(first_article_score)

print(article_texts)
print(article_links)
print(article_upvotes)

# get index of article with the highest number of upvotes, then use that index to get the title and link of the article
largest_number = max(article_upvotes)
most_upvoted_idx = article_upvotes.index(largest_number)

print(article_texts[most_upvoted_idx])
print(article_links[most_upvoted_idx])
