 # -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
		'Cookie':'ServerPool=A; TASSK=enc%3ABuSbKBH03AVSIJSTjebnWsvxieGPPqnqilHq11fUyi%2BlAzpCbUPyh9aKQzILdikIbamtcZtdeWU%3D; TAUnique=%1%enc%3AEm4bmPTyg98CiF4QD4F%2FmzItygYrLSGFD0zoe9L1JO%2BOKebnr7pVIw%3D%3D; TAAuth2=%1%3%3A2382bb4fafe8b47792932bba5098e419%3AACAOkMAb9UijWsC74EkUG%2FGfAAQgO4cKYSBdIujgMtgvkc4hCKWwO8om0kv6IBRqd8hY473R1k1wyC4OCESJeDGZnOU3ldGxkvkFgSjC8zJdvmh59iYVvFZxzrd3HGy%2BJ3B28sdvn4k%2FOXoOJyA0hARsGnCsegKUnUSl4ioUIaA1gTNlx3cJkq6hGafhSyZ%2F7r5URXwbxW6yE5x%2BSZGc%2BYY%3D; _smt_uid=570e48da.461f70c7; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.28953_104l60763_104*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C2%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FTourism-g60763-New_York_City_New_York-Vacations.html; roybatty=ALE%2FyM6sZaHVIUyyiuwKuw%2FW6%2BbseqMPcU%2FBzlCxUQs2pizIjdKfCLQKAZBDGGL9daTWwKhJXnXvqIx5HTvc0A61kKUKLmgRebFomOzWLBBE%2F6%2B%2B71thUnGkIpestPK07Q%3D%3D%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1460449420,1460474214,1460553946; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1460556994; TASession=%1%V2ID.E0537BEA35934C41AD32DC54F477E027*SQ.29*PR.429%7CHome*LS.RecommendedAjax*GR.25*TCPAR.12*TBR.47*EXEX.51*ABTR.89*PPRP.16*PHTB.77*FS.76*CPU.93*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.2F5BF0BD8C1BD0807CF5AF9C5986FE2B*FA.1*DF.0*LP.%2F*MS.-1*RMS.-1*TRA.true*LD.60763; TAUD=LA-1460553947441-1*LG-3047519-2.1.F*LD-3047521-.....; NPID='
		}
url='https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
url_saves='http://www.tripadvisor.cn/Saves#264994'

def get_attractions(url,data=None):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.property_title > a')
	imgs = soup.select('img[width="160"]')
	cates = soup.select(' div.p13n_reasoning_v2')
	for title,img,cate in zip(titles,imgs,cates):
		data = {
		'title':title.get_text(),
		'img':img.get('src'),
		'cate':list(cate.stripped_strings)
		}
		print(data)


def get_favs(url,data=None):	
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('a.location-name')
	imgs = soup.select('img.photo_image')
	metas = soup.select('span.format_address')
	for title,img, meta in zip(titles,imgs,metas):
		data = {
			'title':title.get_text(),
			'img':img.get('src'),
			'meta':list(meta.stripped_strings)
		}
		print(data)
		


#for single_url in urls:
#	get_attractions(single_url)
get_favs(url)
get_attractions(url)