#!/usr/bin/env python

import ntplib
from time import ctime

def printTime():
	ntp_client = ntplib.NTPClient()
	response =  ntp_client.request('http://www.dgut.edu.cn')
	print ctime(response.tx_time)


if __name__ == '__main__':
	printTime()
