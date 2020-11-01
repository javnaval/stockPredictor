import os, sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import cProfile
import json, urllib
from classes.day import Day


url_init = "http://data.fixer.io/api/"
key = "528fee3a5e6eaaa3a359fe949cb22492"
symbols = "EUR,BTC"

for yyyy in range(2015, 2017):
	for mm in range(1, 13):
		for dd in range(1, 29):
			if dd < 10:
				d_s = '0' + str(dd)
			else:
				d_s = str(dd)
			if mm < 10:
				m_s = '0' + str(mm)
			else:
				m_s = str(mm)
			y_s = str(yyyy)
			date = y_s + '-' + m_s + '-' + d_s
			url = url_init + date + '?access_key=' + key + '&symbols=' + symbols
			response = urllib.request.urlopen(url)
			data = json.loads(response.read())
			it_date = "jsonFiles/" + y_s + "-"+ m_s + "-"+ d_s + ".json"
			f= open(it_date,"w")
			f.write(json.dumps(data))
			f.close()

input(" press close to exit ")
