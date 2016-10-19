from bs4 import BeautifulSoup

with open("movie.html","r") as wb_data:
	Soup = BeautifulSoup(wb_data,'lxml')
	movieRating = Soup.select('#screening > div.screening-bd > ul > li:nth-of-type > ul > li.rating')
	movieName = Soup.select('#screening > div.screening-bd > ul > li:nth-of-type > ul > li.title')
	images = Soup.select('#screening > div.screening-bd > ul > li:nth-of-type  > ul > li.poster')


##for info in zip{movieName,movieRating,images}: 605302281930
	print(images)
	print(movieName)
	print(movieRating)
