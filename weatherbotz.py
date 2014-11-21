# Vincent Siu
# Lolol Weatherz
# Should I make this a bot?
# 2014/06/16
# Using World Weather Onlline free API
# All credits go to them for actually gathering the weather data lolz
# Powered by "http://www.worldweatheronline.com/" 
# sauce: https://developer.worldweatheronline.com/page/explorer-free

import urllib2
import json
import xml.etree.ElementTree as ET

def getWeather_JSON():
	#http://developer.worldweatheronline.com
	#Key:
	#2005fce4b3dcf62848d6a262305af50aff6caf4d
	zip = raw_input("What is your zip code? \n >>  ")
	blade = "2005fce4b3dcf62848d6a262305af50aff6caf4d"
	url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q=%s&format=json&extra=localObsTime&includelocation=yes&key=2005fce4b3dcf62848d6a262305af50aff6caf4d" %zip
	dataz = urllib2.urlopen(url)
	JSON = dataz.read()
	dataz.close()

	weather_dict = json.loads(JSON)
	current_temp_C = weather_dict['data']['current_condition'][0]['temp_C']
	current_temp_F = weather_dict['data']['current_condition'][0]['temp_F']
	current_city = weather_dict['data']['nearest_area'][0]["areaName"][0]["value"]

	print "The weather conditions today for %s:" % current_city
	print "The weather right now is %s degrees Celcius, or %s degrees Farenheit." % (current_temp_C, current_temp_F)

def getWeather_XML():
	#http://developer.worldweatheronline.com
	#Key:
	#2005fce4b3dcf62848d6a262305af50aff6caf4d
	zip = raw_input("What is your zip code? \n >>  ")
	blade = "2005fce4b3dcf62848d6a262305af50aff6caf4d"
	url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q=%s&format=xml&extra=localObsTime&includelocation=yes&key=2005fce4b3dcf62848d6a262305af50aff6caf4d" %zip
	dataz = urllib2.urlopen(url)
	XML = dataz.read()
	dataz.close()
	parsed = ET.fromstring(XML)
	current_temp_C = parsed[2][2].text
	current_temp_F = parsed[2][3].text
	current_city = parsed[1][0].text
	print "The weather conditions today for %s:" % current_city
	print "The weather right now is %s degrees Celcius, or %s degrees Farenheit." % (current_temp_C, current_temp_F)

#getWeather_JSON()
#getWeather_XML()