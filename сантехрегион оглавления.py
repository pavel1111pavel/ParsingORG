import requests
from bs4 import BeautifulSoup
from requests.api import head
import re

def resp(url):
    s = requests.Session()
    response = s.get(url = url)
     soup = BeautifulSoup(response.content, 'html.parser')
    x = soup.find_all('ul', class_ = 'tree')

    with open('links.txt', 'w') as f:
        for i in soup.find_all('ul', class_='tree'):
            links = i.find_all('a', href=True)
            for link in links:
                href = link.get('href')
                if href:
                    f.write('http://ORG.com' +href + '\n')


    with open('ORG sublinks.txt', 'w') as f:
        with open('links.txt', 'r') as f_links:
            for line in f_links:
                link = line.strip()
                s = requests.Session()
                response = s.get(url=link)
                print(response)
                soup = BeautifulSoup(response.content, 'html.parser')
                x = soup.find_all('ul', class_='sub-links')
                for i in x:
                    hrefs = i.find_all('a', href=True)
                    for href in hrefs:
                        link = href.get('href')
                        if link:
                            f.write('http://ORG.com' + link + '\n')
                            print('+'*10)

    with open('ORG ID_product.txt', 'w') as id:
        with open('ORG sublinks.txt', 'r') as f:
            for line in f:
                url = line.strip()
                s = requests.Session()
                response = s.get(url=url)
                soup = BeautifulSoup(response.content, 'html.parser')
                x = soup.find_all('div', class_='image')
                time.sleep(3)
                for i in x:
                    img_src = i.find('img')['src']
                    match = re.search(r'/(\d+)/images', img_src)
                    if match:

                        product_id = match.group(1)
                        id.write(product_id + '\n')
                        print(product_id)

def main():

    resp(url = 'http://ORG.com/')

if __name__ == '__main__':
    main()
