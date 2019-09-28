from flask import request

# Module: surorise.py
expectedFields = ['time', 'location', 'categories']


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
