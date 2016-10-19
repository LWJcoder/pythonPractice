#coding: utf-8
money = 10
price = 2
pingshu = 5
pgai = 5 ##ping gai = 5
kping = 5 ##ping shu =5
pgaidhnum = 4
kpingdhnum = 2

def pingzi():
	global kping
	global pingshu
	global pgai
	while True:
		c = kping/kpingdhnum
		#reduce dui huan de 
		print "c: "
		print c
		print"*********************************"
		kping-=c*kpingdhnum

		#add the new dui huan de
		
		pgai+=c
		
	
		print "kping: " 
		print kping
		if pingshu<2:
			pinggai()
			break
def pinggai():

	global pgai
	global pgaidhnum
	while True:
		a = pgai/pgaidhnum
		print "a: "
		print a
		print"*********************************"
		pgai-=a*pgaidhnum

		b = pgai%pgaidhnum
		kping=a+kping
		print  "pgai: "
		print pgai
		if pgai<4:
			pingzi()
			break


if __name__ == '__main__':
	pingzi()