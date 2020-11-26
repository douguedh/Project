

import requests
import bs4

dateList = []
higlist = []
lowlist= []

r = requests.get(
    'https://coinmarketcap.com/currencies/bitcoin/historical-data/')
soup = bs4.BeautifulSoup(r.text, "lxml")

tr = soup.find_all('tr',{'class':'text-right'})
for item in tr:
    dateList.append(item.find('td', {'class':'text-left'}).text)