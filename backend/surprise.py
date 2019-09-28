from flask import request, jsonify
import pandas as pd
import sbb
# Module: surprise.py

# Module: surprise.py

expectedFields = ['date', 'locationId', 'categories']


def main():
    assert request.method == 'POST'
    data = request.get_json()

    missing = checkJson(expectedFields, data)
    if missing:
        print('Missing field: %s' % missing)
        return 'Missing field: %s' % missing

    originLocation = data['locationId']

    # get all proper stations filtered by categories
    categories = data['categories']
    df = getCSV()
    columns = list(df.columns)

    # check if a category is not in the column
    invalid = categoriesNotValid(categories, columns)
    if invalid:
        print('Invalid category %s' % invalid)
        return 'Invalid category %s' % invalid

    for category in categories:
        filtered_categories = df[category] > 0
        df = df[filtered_categories]

    # rank stations by amount of the categories
    df = df.sort_values(by=categories, ascending=False)

    # TODO: filter it more by possible attributes: weather, previous commutes or events
    stationLocations = list(
        filter(lambda UIC: UIC is not originLocation, df['UIC'].tolist()))

    trips = list(map(lambda stationId: sbb.getReturnTrip(
        originLocation, stationId, date=data['date']), stationLocations))
    print(trips)
    return jsonify(trips)


def checkJson(expectedFields, data):
    if not data:
        return 'data'

    for f in expectedFields:
        try:
            data[f]
        except:
            return f


def getCSV():
    return pd.read_csv("fakeData.csv")  # csv file which you want to import


def categoriesNotValid(categories, columns):
    for category in categories:
        if category not in columns:
            return category
