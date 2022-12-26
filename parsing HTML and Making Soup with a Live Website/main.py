from bs4 import BeautifulSoup
import requests

# Remember a change to the source code from website will affect the codes below
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title.string)

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    print(article_texts)
    print(article_links)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
print(int(article_upvotes[0].split()[0]))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# '\n'
# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.getText("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
