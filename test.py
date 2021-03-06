import json
import random
import googleAPI_handler
import requests

url = 'http://localhost:5000/insert_sensor/'
headers = {'content-type': 'application/json'}
#response = requests.post(url, data=json.dumps(data), headers=headers)


#import mysql.connector


#print('before')
#mysql.connector.connect(host='35.241.162.141', database='mysql', user='root', password='')
#mysql.connector.connect(host='localhost', database='mysql', user='root', password='Password1', port=3307)
#print ('after')
#pass

mydict = {
    "id": None,
    "address": None,
    'capacity': None,
    'status': None,
    'lat': None,
    'lng': None
}
'''

index = 1
for i in range(1, 100):
    mydict['id'] = random.randint(1, 30)
    mydict['capacity'] = random.randint(1, 100)
    if random.randint(0, 1):
        mydict['status'] = 'ok'
    else:
        mydict['status'] = 'broken'
    mydict['lat'] = random.randint(1, 120)
    mydict['lng'] = random.randint(1, 120)
    response = requests.post(url, data=json.dumps(mydict), headers=headers)
    print(index)
    index = index + 1
'''

total_list = []
city_name = 'Ramat+Gan+'
streets = ['Hamelacha', 'Anne+Frank+', 'Yeda+Am+', 'Brurya', 'Yehudit', 'Charusim']
streets_numbers = [16, 30, 21, 5, 13, 14]
st_s = ['Anne+Frank+', 'Yeda+Am+']
st_n_s = [30, 21]


print("create all addresses from google api")
index = 0
for i in range(0, len(streets)):
    total_list.append(googleAPI_handler.get_cords_by_full_address(city_name, streets[i], streets_numbers[i]))
'''
n_list = []
for li in total_list:
    n_list.append(list(set(li)))
'''

print("insert all sensors to our db")
index = 1
sumlist = sum(streets_numbers)
count_id = 1000
for street in total_list:
    for house in street:
        mydict['id'] = str(count_id)
        mydict['address'] = house['full_address']
        mydict['capacity'] = random.randint(1, 100)
        if random.randint(0, 1):
            mydict['status'] = 'online'
        else:
            mydict['status'] = 'offline'
        mydict['lat'] = float(house['lat'])
        mydict['lng'] = float(house['lng'])
        response = requests.post(url, data=json.dumps(mydict), headers=headers)
        print(str(index) + " of : " + str(sumlist))
        index = index + 1
        count_id = count_id + 1

