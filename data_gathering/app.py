import requests
import csv
from geopy import distance

# start csv with the column headers
def startCSVFile():
    token = getSBBToken()
    with open('stationData.csv', mode='w', newline='', encoding='utf-8') as stationData_file:
        fieldnames = ['UIC','station','latitude','longitude','mountain','castle','swim','shopping_mall','amusement_park','art_gallery','museum']
        stationData_writer = csv.DictWriter(stationData_file, fieldnames=fieldnames)
        stationData_writer.writeheader()
        getAllStationsAndTheirLocation(stationData_writer,token)

# get a list of all stations together with the location (lat,long)
def getAllStationsAndTheirLocation(writer,token):
    max_site = 20
    curr_site = 1

    while curr_site <= max_site:
        print('site: %s ' %curr_site)
        url = 'https://data.sbb.ch/api/records/1.0/search/'
        dataset = 'betriebspunkte-didok'
        rows = '20'
        start = curr_site
        sort = '-didok85'
        refine = '*'
        params = {
            'dataset': dataset,
            'rows': rows,
            'start': start,
            'sort': sort,
            'refine.haltestelle': refine
        }

        request = requests.get(url = url, params = params)

        data = request.json()
        records = data['records']
        for record in records:
            locationId = record['fields']['bpuic']
            if(locationDoesNotExist(locationId,token)):
                next
            name = record['fields']['gdname']
            latitude = record['fields']['geopos'][0]
            longitude = record['fields']['geopos'][1]
            places = getPlacesOfALocation(latitude,longitude)
            writer.writerow({'UIC':locationId,'station':name,'latitude':latitude,'longitude':longitude,'mountain': places['mountain'],'castle':places['castle'],'swim':places['swim'],'shopping_mall':places['shopping mall'],'amusement_park':places['amusement park'],'art_gallery':places['art gallery'],'museum':places['museum']})


        
        curr_site = curr_site+1


# for each station
# get places of a query based on location (for each query)
def getPlacesOfALocation(latitude,longitude):
    maxDistance = 2
    maxNumberPlaces = 10
    categories = ['mountain', 'castle', 'swim', 'shopping mall', 'amusement park', 'art gallery', 'museum']
    result = {}

    for category in categories:
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        query = category
        location = '%s,%s' %(latitude,longitude)
        radius = '200'
        # don't publish the API key
        key = 'xxxxxx'

        params = {
            'query': query,
            'location': location,
            'radius': radius,
            'key': key
        }

        request = requests.get(url = url, params = params)

        data = request.json()
        places = data['results'][:maxNumberPlaces]
        counter = 0
        for place in places:
            placeLatitude = place['geometry']['location']['lat']
            placeLongitude = place['geometry']['location']['lng']
            placeDistance = distance.distance((float(latitude),float(longitude)), (float(placeLatitude),float(placeLongitude))).km
            if placeDistance < maxDistance:
                counter = counter+1
        result[category] = counter

    return result

def getSBBToken():
    url = 'https://sso-INT.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token'
    data = {"grant_type": "client_credentials", "client_id": "22ebc2be",
            "client_secret": "2c820784f3e28837959abc43120989ca"}
    try:
        result = requests.post(url, data=data)
        return result.json()['access_token']
    except Exception as e:
        print(e)


def locationDoesNotExist(destinationId,token):
    url = 'https://b2p-int.api.sbb.ch/api/trips'
    headers = {"Authorization": token, "X-Contract-Id": "HAC222P",
               "X-Conversation-Id": "cafebabe-0815-4711-1234-ffffdeadbeef"}
    params = {"originId": "8503000", "destinationId": destinationId,
              "date": "2019-10-02", "time": "10:22"}
    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
        return False
    except Exception as e:
        return True


startCSVFile()