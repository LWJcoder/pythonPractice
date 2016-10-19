from bs4 import BeautifulSoup


with open("movie.html","r") as wb_data:
	Soup = BeautifulSoup(wb_data,'lxml')
	movieRating = Soup.select('#gaia > div.list-wp > div > a:nth-of-type> p > strong')
	movieName = Soup.select('#screening > div.screening-bd > ul > li:nth-of-type > ul > li.title')
	images = Soup.select('#screening > div.screening-bd > ul > li:nth-of-type  > ul > li.poster')
	cate = Soup.select('#info > span:nth-of-type')
	print(movieName,movieRating)


for movieName,movieRating,images,cate in zip(movieName,movieRating,images,cate):
	data = {
		'movieName':movieName.get_text(),
		'movieRating':movieRating.get_text(),
		'images':images.get('src'),
		'cate':list(cate.stripped_strings)
	}
	for i in data:
		if(float(i['movieRating'])>3):
			print(i['movieName'],i['cate'])


##for info in zip{movieName,movieRating,images}: 605302281930#screening > div.screening-bd > ul > li:nth-of-type > ul > li.rating
#vzaso