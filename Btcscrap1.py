from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import pandas as pd

BTC = []

def price():
  try:
    url = 'https://www.google.com/search?q=bitcoin+price'
    Html = requests.get(url)
		soup = BeautifulSoup(Html.text,'html.parser')
		text = soup.find('div', attrs = {'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs = {'class':'BNeawe iBp4i AP7Wnd'}).text 
		return text
   except:
    print('you are not connected to the internet')
  
 def main():
	lprice = -1
	while True:
		crypto = ''
		bei = price()
		saa = datetime.now()
		if bei != lprice:
			print(bei, saa)
			lprice = bei
			BTC.append(lprice)
		time.sleep(3)
	
main()	
