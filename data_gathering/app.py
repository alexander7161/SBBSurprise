import requests
import csv
from geopy import distance

# start csv with the column headers
def startCSVFile():
    with open('stationData.csv', mode='w', newline='', encoding='utf-8') as stationData_file:
        fieldnames = ['locationId','station','latitude','longitude','mountain','castle','swim_place','shopping_mall','amusement_park','art_gallery','museum']
        stationData_writer = csv.DictWriter(stationData_file, fieldnames=fieldnames)
        stationData_writer.writeheader()
        getAllStationsAndTheirLocation(stationData_writer)

# get a list of all stations together with the location (lat,long)
def getAllStationsAndTheirLocation(writer):
    max_site = 20
    curr_site = 1

    while curr_site <= max_site:
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
            name = record['fields']['gdname']
            latitude = record['fields']['geopos'][0]
            longitude = record['fields']['geopos'][1]
            places = getPlacesOfALocation(latitude,longitude)
            writer.writerow({'locationId':locationId,'station':name,'latitude':latitude,'longitude':longitude,'mountain': places['mountain'],'castle':places['castle'],'swim_place':places['swim'],'shopping_mall':places['shopping mall'],'amusement_park':places['amusement park'],'art_gallery':places['art gallery'],'museum':places['museum']})


        
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


startCSVFile()