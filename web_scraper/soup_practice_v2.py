from bs4 import BeautifulSoup
import requests

# disallowed stuff bots should not be scraped"https://news.ycombinator.com/news/robots.txt", scrape <1/min

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

soup_title = soup.find(class_="titleline")

article_link = soup_title.find('a', href=True)

article_upvote = soup.find(class_="score")

# article_link["href"] same as article_link.get("href")
#print(soup_title.getText(), article_link.get("href"), article_upvote.getText())


soup_titles = soup.find_all(class_="titleline")
article_upvotes = soup.find_all(class_="score")

# gets highest upvoted article
article_upvote_nums = [int((x.get_text()).split(' ')[0]) for x in article_upvotes]
upvote_max = max(article_upvote_nums)
highest_upvoted_index = article_upvote_nums.index(upvote_max)
highest_upvoted_href = soup_titles[highest_upvoted_index].find('a', href=True)
print(soup_titles[highest_upvoted_index].get_text(), highest_upvoted_href.get("href"), upvote_max)

"""
for title in soup_titles:
    print(title.getText(), title.find('a', href=True))
"""

