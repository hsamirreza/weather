import requests

lon= input('Enter Longtitude: ')
#tool geography az user gerefte mishavad
lat= input('Enter Latitude: ')
#arz geography az user gerefte mishavad
weather = requests.get('http://api.openweathermap.org/data/2.5/find?lat=%s&lon=%s&cnt=5&appid=96621c11a25325037ec2980de8d5b114'%(lat,lon))
#az site openweatermap information location khaste shode ba 1 circle va 5 shahr grefte mishavad
temperature1 = weather.json()['list'][int()]['main']['temp']
#az weather item 'temp' station 1 ra estekhraj mikonad
temperature2 = weather.json()['list'][int(1)]['main']['temp'] #az weather item 'temp' station 2 ra estekhraj mikonad
temperature3 = weather.json()['list'][int(2)]['main']['temp'] #az weather item 'temp' station 3 ra estekhraj mikonad
temperature4 = weather.json()['list'][int(3)]['main']['temp'] #az weather item 'temp' station 4 ra estekhraj mikonad
temperature5 = weather.json()['list'][int(4)]['main']['temp'] #az weather item 'temp' station 5 ra estekhraj mikonad
average_temperature = (temperature1+temperature2+temperature3+temperature4+temperature5)/5
print('average temperature is: ',average_temperature)