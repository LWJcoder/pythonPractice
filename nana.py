from bs4 import BeautifulSoup
import requests
import re
import time

path = 'C:\\pythonFile\\movie300page.txt'
movie_jinghua_title_url = 'http://nanabt.com/index.php?c=thread&fid=6&tab=digest'
movie_urls = ['http://nanabt.com/index.php?c=thread&fid=6&page={}'.format(str(i)) for i in range(2,3,1)]


#LoR > div.main_wrap > div.main.cc > div.ga07.clpd1.fl.forum_page > div.bbs_info_box.cc > dl:nth-child(1) > dd
#LoR > div.main_wrap > div.main.cc > div.ga07.clpd1.fl.forum_page > div.bbs_info_box.cc > dl:nth-child(2) > dd
#LoR > div.main_wrap > div.main.cc > div.ga07.clpd1.fl.forum_page > div.bbs_info_box.cc > dl.clpd1.info_highest > dd
#LoR > div.main_wrap > div.main.cc > div.ga07.clpd1.fl.forum_page > div.bbs_info_box.cc > dl.clpd1.info_postTotal > dd

#J_posts_list > div:nth-child(1) > div.counter > span.hits  
#J_posts_list > div:nth-child(1) > div.counter > span.replies

#J_posts_list > div.cc.polist.listop > div.counter > span.hits
##J_posts_list > div.cc.polist.listop > div.subject > p.title > a
##J_posts_list > div:nth-child(7) > div.subject > p.title > a
##J_posts_list > div:nth-child(7) > div.subject > p.info > span:nth-child(4)
def get_attractions(url,data=None):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.subject > p.title > a')
	infos = soup.select('div.subject > p.info > span:nth-of-type')
	hits = soup.select('div.counter > span.hits')
	replies = soup.select('div.counter > span.replies')
	
	

	

	for title, info, hit, reply in zip(titles,infos,hits,replies):
		titles = get_the_text(titles)
		infos = get_the_text(infos)
		hits = get_the_text(hits)
		replies = get_the_text(replies)

		data = {
		'title': list(titles),
		'info':list(infos),
		'hit':list(hits),
		'reply':list(replies)
		}
		
		
		
		

def get_the_text(dd):
	dr = re.compile(r'<[^>]+>', re.S)
	dd = dr.sub('', str(dd))
	print(dd+'\n')

	
	

def writeFile(path,obj,data=None):
	#write to file

	f_obj = open(path, 'w')
	for object1 in obj:
		f_obj.write(str(object1))
		f_obj.write("\n")
	f_obj.close()


for str_url in movie_urls:
	get_attractions(str_url)
	time.sleep(0.3)	
	