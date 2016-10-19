from bs4 import BeautifulSoup
import requests

headers = {
	'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
	#'Cookie':'ServerPool=C; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7Csh%2C%2C-1%7C2016sticksess%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C1%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; TASSK=enc%3ADwDm2iMJIKW5DjIwVuP3%2FsvxieGPPqnq5JnrzOR5Xa9ZD2jMfSEwjdaKQzILdikIbamtcZtdeWU%3D; TAUnique=%1%enc%3A2OiwKVkXffUCiF4QD4F%2FmzItygYrLSGFTluPg0j9ppMWghrtO0p0rQ%3D%3D; roybatty=AMa9jIXhyoenNpgx2w0PWVfwrZLh%2FKaiCyKuSRMIZLLM3ybBI8coqXqeWXjG3o29ziPHMSbqE%2BZVRdw71beI3czfK%2F2gKKvz%2BQvP6yXELkRdtQKsskkqgnu7PWkjcUT8Qw%3D%3D%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1460449420,1460474214,1460553946,1460706177; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1460706177; TASession=%1%V2ID.A26254299DB6F0A149302F1437EBB090*SQ.4*LS.DaoDaoStaticVelocityPageAjax*GR.61*TCPAR.46*TBR.76*EXEX.62*ABTR.71*PPRP.22*PHTB.93*FS.70*CPU.10*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*FLO.60763*TRA.true*LD.60763; TAUD=LA-1460706176707-1*LG-3422-2.1.F*LD-3424-.....; NPID='
}

url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

wb_data = requests.get(url,headers = headers)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')

for i in imgs:
	print(i.get('src'))