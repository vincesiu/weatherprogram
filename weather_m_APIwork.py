# Vincent Siu
# 20140623
# Weather module

import urllib2
import json

def getCurrentWeather(zip):
	"""returns a list in unicode encoding, in format: current temp C, current temp F, 
	current city, current conditions; if zipcode does not exist, returns [-1, -1, -1]"""
	weather_dict = dataz(zip)
	if 'error' in weather_dict['data']:
		values = [-1,-1,-1,-1]
		return values
	else:
		current_temp_C = weather_dict['data']['current_condition'][0]['temp_C']
		current_temp_F = weather_dict['data']['current_condition'][0]['temp_F']
		current_city = weather_dict['data']['nearest_area'][0]["areaName"][0]["value"]
		current_condition = weather_dict['data']['current_condition'][0]['weatherDesc'][0]['value']
		values = [current_temp_C, current_temp_F,current_city,current_condition]
		return values

def debugger():
	"""example output: [u'16', u'61', u'Millbrae', u'Clear']""" 
	values = getCurrentWeather(94030)
	print values

def dataz(zip):
	"""returns json data in dictionary format"""
	#http://developer.worldweatheronline.com
	#Key:
	#2005fce4b3dcf62848d6a262305af50aff6caf4d
	blade = "2005fce4b3dcf62848d6a262305af50aff6caf4d"
	url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q=%s&format=json&extra=localObsTime&includelocation=yes&key=2005fce4b3dcf62848d6a262305af50aff6caf4d" %zip
	packed_data = urllib2.urlopen(url)
	unpacked_data = packed_data.read()
	packed_data.close()
	weather_dict = json.loads(unpacked_data)
	return weather_dict
