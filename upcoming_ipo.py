from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests
html_text=requests.get('https://zerodha.com/ipo/').text
soup= BeautifulSoup(html_text,'lxml')
iposection=soup.find('section', id='ipo')
upcoming_ipo_talbe = iposection.find('tbody')
ipotable = PrettyTable(["Stock","IPO Date","Listing date","Price Range","Min qty","RHPV link"])
n=len(upcoming_ipo_talbe.find_all("tr")) # no.of upcoming IPOs
row=upcoming_ipo_talbe.find('tr')
for i in range (n):
    stock=row.td                                                     #stock name
    date=stock.next_sibling.next_element                             #IPO date
    listing_date=date.next_sibling.next_element                      #listing date
    price_range=listing_date.next_sibling.next_element               #price range
    min_qnt=price_range.next_sibling.next_element                    #min quantity  
    rhp_link=min_qnt.next_sibling.next_element.find('a').get('href') #rhp link
    row=row.next_sibling.next_element
    ipotable.add_row([stock.text.lstrip().rstrip(),date.text.lstrip().rstrip(),listing_date.text.lstrip().rstrip(),price_range.text.lstrip().rstrip(),min_qnt.text.lstrip().rstrip(),rhp_link])
    
print(ipotable)

