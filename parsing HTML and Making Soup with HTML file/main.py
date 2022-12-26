from bs4 import BeautifulSoup


with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
'\n'
all_paragraph_tags = soup.find_all(name="p")
print(all_paragraph_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.getText("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
