from flask import request
import pandas as pd

# Module: surprise.py


def main():
    assert request.method == 'POST'
    data = request.get_json()

    missing = checkJson(expectedFields, data)
    if missing:
        print('Missing field: %s' % missing)
        return 'Missing field: %s' % missing

    print(data)

    # get all proper stations filtered by categories
    categories = data.categories
    df = getCSV()
    columns = list(df.columns)

    # check if a category is not in the column
    invalid = checkCategoriesInColumns(categories,columns)
    if invalid:
        print('Invalid category %s' % invalid)
        return 'Invalid category %s' % invalid
    

    for category in categories:
        filtered_categories = df[category]>0
        df = df[filtered_categories]

    # rank stations by amount of the categories they've got
    df = df.sort_values(by=categories,ascending=False)

    # filter it more by possible attributes: weather, previous commutes or events

    # get the station details from the locationId (SBB)

    # take a limited amount (ranked by what?) of 15 and request travel details from starting station (locationId) until surprise station (get travel price and time)

    # sort by prive and time

    # return Array of the places
    return "surprise"


def checkJson(expectedFields, data):
    if not data:
        return 'data'

    for f in expectedFields:
        try:
            data[f]
        except:
            return f

def getCSV():
    return pd.read_csv("fakeData.csv") #csv file which you want to import

def checkCategoriesInColumns(categories, columns):
    for category in categories:
        if category not in columns:
            return category


expectedFields = ['time', 'locationId', 'categories']
