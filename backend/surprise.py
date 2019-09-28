from flask import request
import pandas as pd

# Module: surorise.py


def main():
    assert request.method == 'POST'
    data = request.get_json()

    missing = checkJson(expectedFields, data)
    if missing:
        print('Missing field: %s' % missing)
        return 'Missing field: %s' % missing

    print(data)
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
    df = pd.read_csv("fakeData.csv") #csv file which you want to import
    return df.to_string()



expectedFields = ['time', 'locationId', 'categories']
