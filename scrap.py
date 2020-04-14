import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail 
from datetime import date

urls = ["https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"]

headers ={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'} 

today = str(date.today()) + ".csv"

csv_file  = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask','Day Range','52 Week Range','Volume','Avg. Volume'])

for url in urls:
	stock=[]

	html_page =requests.get(url,headers=headers)

	#print(html_page.content)
 
	soup = BeautifulSoup(html_page.content,'lxml')

	#print(soup.title)

	#title = soup.find("title").get_text()

	#print(title)

	# For filtering required data 

	header_info = soup.find_all("div",id="quote-header-info")[0]

	stock_title = header_info.find("h1").get_text()


	#for extracting current price

	current_price = header_info.find("div", class_ = "My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()

	stock.append(stock_title)

	stock.append(current_price)

	#print(stock_title)

	#print(current_price)

	#for extracting table content

	table_info = soup.find_all("div",class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


	#previous_close_heading = table_info[0].find_all("td")[0].get_text()

	#previous_value = table_info[0].find_all("td")[1].get_text()

	#print("{0} - {1}".format(previous_close_heading,previous_value))

	#for extracting table content - ||

	for i in range(0,8):
		
		#previous_close_heading = table_info[i].find_all("td")[0].get_text()

		previous_value = table_info[i].find_all("td")[1].get_text()

		stock.append(previous_value)

		#print("{0} - {1}".format(previous_close_heading,previous_value))

	csv_writer.writerow(stock)

	time.sleep(5)

csv_file.close()

send_mail.send(filename=today)