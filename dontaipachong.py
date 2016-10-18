from bs4 import BeautifulSoup
from sqlite3 import connect
import requests
import time

url = "https://knewone.com/discover?page="


def get_page(url,data = None):

	wb_data = requests.get(url)
	Soup = BeautifulSoup(wb_data.text,'lxml')

	imgs = Soup.select('a.cover-inner > a > img')
	titles = Soup.select('section.content > h4 > a')
	links =  Soup.select('section.content > h4 > a')

	saveData(imgs, titles, links)
			
def saveData(imgs, titles, links):
	conn = connect(r'C:\pythonFile\temp3.db')
	curs = conn.cursor()
	curs.execute('create table emp3 (imgs, titles, links)')
	prefix = "insert into emp values (%s,%s,%s)"
	curs.execute(prefix+(imgs, titles, links))
	curs.execute("select * from emp")
	for(imgs, titles, links) in curs.fetchall():
		print(imgs, titles, links)

def get_more_pages(start,end):
	for One in range(start,end):
		url_c = url+str(One)
		get_page(url_c)
		time.sleep(2)



if __name__ == '__main__':
	get_more_pages(1,10)