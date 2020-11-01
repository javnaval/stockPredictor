import os, sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import cProfile
import json, urllib
import matplotlib.pyplot as plt

dates = []
valuesBTC = []

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
			it_date = "jsonFiles/" + y_s + "-"+ m_s + "-"+ d_s + ".json"
			f = open(it_date,"r")
			json_f=json.loads(f.read())
			dates.append(json_f["date"])
			valuesBTC.append(1/float(json_f["rates"]["BTC"]))
			f.close()
plt.plot(dates, valuesBTC)
plt.ylabel('Values of BTC in dates')
plt.show()
