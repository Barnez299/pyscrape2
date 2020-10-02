
import requests
from bs4 import BeautifulSoup
import csv



url = 'https://pythonprogramming.net/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

csv_file = open('my_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['title','summary','weblink'])


articles = soup.find_all('div', class_='card-panel hoverable')

for item in articles:
    title = item.find('span', class_='card-title').text
    summary = item.find('p').text.strip()
    link = item.find('a')['href']

    weblink = f'https://pythonprogramming.net{link}'

    
    pysumm ={
        'title': title,
        'summary': summary,
        'weblink': weblink
    }

    csv_writer.writerow([title, summary, weblink])

csv_file.close()
   














