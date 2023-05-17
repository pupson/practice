from bs4 import BeautifulSoup
import lxml

with open('website.html') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

"""
# print title string (.name prints 'title')
print(soup.title.string)
# print indented html code
print(soup.prettify())
# paragraphs
print(soup.p)
# print all anchor tags
print(soup.find_all(name="a"))
"""
"""
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:

    # prints all anchor text
    print(tag.getText())
    # prints all links
    print(tag.get("href"))
"""

heading = soup.find(name="h1", id="name")
print(heading)

# print a list of all headings
class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

# print first heading text
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get_text())

# css
company_url = soup.select_one(selector="p a")
print(company_url)

# css
company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(".heading")
print(headings)