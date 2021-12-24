import requests
import math
lon= float(input('Enter Longtitude: '))
#tool geography az user gerefte mishavad
lat= float(input('Enter Latitude: '))
#arz geography az user gerefte mishavad
weather = requests.get('http://api.openweathermap.org/data/2.5/find?lat=%i&lon=%i&cnt=5&appid=96621c11a25325037ec2980de8d5b114'%(lat,lon))
#az site openweatermap information location khaste shode ba 1 circle va 5 shahr grefte mishavad
temperature1 = weather.json()['list'][0]['main']['temp']
#az weather item 'temp' station 1 ra estekhraj mikonad
temperature2 = weather.json()['list'][1]['main']['temp'] #az weather item 'temp' station 2 ra estekhraj mikonad
temperature3 = weather.json()['list'][2]['main']['temp'] #az weather item 'temp' station 3 ra estekhraj mikonad
temperature4 = weather.json()['list'][3]['main']['temp'] #az weather item 'temp' station 4 ra estekhraj mikonad
temperature5 = weather.json()['list'][4]['main']['temp'] #az weather item 'temp' station 5 ra estekhraj mikonad
long1 = weather.json()['list'][0]['coord']['lon'] #tool station 1
long2 = weather.json()['list'][1]['coord']['lon']
long3 = weather.json()['list'][2]['coord']['lon']
long4 = weather.json()['list'][3]['coord']['lon']
long5 = weather.json()['list'][4]['coord']['lon']
lat1 = weather.json()['list'][0]['coord']['lat'] #arz station 1
lat2 = weather.json()['list'][1]['coord']['lat']
lat3 = weather.json()['list'][2]['coord']['lat']
lat4 = weather.json()['list'][3]['coord']['lat']
lat5 = weather.json()['list'][4]['coord']['lat']
delta_long1 = long1 - lon #ekhtelaf tool station 1 va location dade shode
delta_long2 = long2 - lon
delta_long3 = long3 - lon
delta_long4 = long4 - lon
delta_long5 = long5 - lon
delta_lat1 = lat1 - lat #ekhtelaf arz station 1 va location dade shode
delta_lat2 = lat2 - lat
delta_lat3 = lat3 - lat
delta_lat4 = lat4 - lat
delta_lat5 = lat5 - lat
distance1 = math.sqrt((delta_lat1)**2 + (delta_long1)**2) #fasele station 1 va location dade shode
distance2 = math.sqrt((delta_lat2)**2 + (delta_long2)**2)
distance3 = math.sqrt((delta_lat3)**2 + (delta_long3)**2)
distance4 = math.sqrt((delta_lat4)**2 + (delta_long4)**2)
distance5 = math.sqrt((delta_lat5)**2 + (delta_long5)**2)
wz1 = temperature1/((distance1)**2)
wz2 = temperature2/((distance2)**2)
wz3 = temperature3/((distance3)**2)
wz4 = temperature4/((distance4)**2)
wz5 = temperature5/((distance5)**2)
w1 = 1/((distance1)**2) #mohasebe makhraj formol IDW
w2 = 1/((distance2)**2)
w3 = 1/((distance3)**2)
w4 = 1/((distance4)**2)
w5 = 1/((distance5)**2)
local_tempreture = (wz1+wz2+wz3+wz4+wz5)/(w1+w2+w3+w4+w5) #formol IDW
print('temperature is: ',local_tempreture)