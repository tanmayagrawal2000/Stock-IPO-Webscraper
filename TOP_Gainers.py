from prettytable import PrettyTable
from bs4 import BeautifulSoup
import requests
html_text=requests.get('https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php').text
soup= BeautifulSoup(html_text,'lxml')
top_table=soup.find('div', class_='bsr_table hist_tbl_hm')
comp_table=top_table.find('tbody')
comp_rows=comp_table.find('tr')
myTable = PrettyTable(["Company Name","High","Low","Last Price","Prev Close","Change","Gain %"])
for i in range(8):
    name=comp_rows.td.span.h3.a.text
    high=comp_rows.next_element.next_element.next_sibling.next_sibling
    low=high.next_sibling.next_element
    last_price=low.next_sibling.next_element
    prev_close=last_price.next_sibling.next_element
    change=prev_close.next_sibling.next_element
    gain=change.next_sibling.next_element
    # print(name)
    # print(high.text)
    # print(low.text)
    # print(last_price.text)
    # print(prev_close.text)
    # print(change.text)
    # print(gain.text)    
    myTable.add_row([name,high.text,low.text,last_price.text,prev_close.text,change.text,gain.text])
    comp_rows=comp_rows.next_sibling.next_element
print(myTable)