from requests_html import HTMLSession
session = HTMLSession()

# URL for topic = World
url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'
r = session.get(url)

r.html.render(sleep=1, scrolldown=0)

articles = r.html.find('article')

for item in articles:
    newsitem = item.find('a', first=True)
    link = newsitem.absolute_links
    print(link)
