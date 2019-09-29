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

    def rowBelongsToCategory(row):
        dictRow = row._asdict()
        for category in categories:
            if dictRow[category] > 0:
                return True
        return False
    df = df.sort_values(by=categories, ascending=False)

    df = pd.DataFrame(list(filter(lambda row: rowBelongsToCategory(row), df.itertuples())))

    # rank stations by amount of the categories

    # TODO: filter it more by possible attributes: weather, previous commutes or events

    stationLocations = list(
        filter(lambda UIC: UIC is not originLocation, df['UIC'].tolist()[:3]))

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
    return pd.read_csv("data.csv") #csv file which you want to import

def categoriesNotValid(categories, columns):
    for category in categories:
        if category not in columns:
            return category
