import requests
import json


def getSBBToken():
    url = 'https://sso-INT.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token'
    data = {"grant_type": "client_credentials", "client_id": "22ebc2be",
            "client_secret": "2c820784f3e28837959abc43120989ca"}
    try:
        result = requests.post(url, data=data)
        return result.json()
    except Exception as e:
        print(e)


def getTripId(originId, destinationId, date, time, token):
    url = 'https://b2p-int.api.sbb.ch/api/trips'
    headers = {"Authorization": token, "X-Contract-Id": "HAC222P",
               "X-Conversation-Id": "cafebabe-0815-4711-1234-ffffdeadbeef"}
    params = {"originId": originId, "destinationId": destinationId,
              "date": date, "time": time}
    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
        return data[0]
    except Exception as e:
        print(e)
        print(data)


def getTripPrice(tripId, token):
    url = 'https://b2p-int.api.sbb.ch/api/v2/prices'
    headers = {"Authorization": token, "X-Contract-Id": "HAC222P",
               "X-Conversation-Id": "cafebabe-0815-4711-1234-ffffdeadbeef"}
    params = {"passengers": "paxa;42;half-fare", "tripIds": tripId}
    try:
        res = requests.get(url, headers=headers, params=params)
        return res.json()[0]
    except Exception as e:
        print(e)


def getTrip(originId, destinationId, date, time):
    token = getSBBToken()['access_token']
    trip = getTripId(originId, destinationId, date, time, token)
    tripId = trip['tripId']
    tripPrice = getTripPrice(tripId, token)['price']
    return {"price": tripPrice, "segments": trip['segments']}


def getReturnTrip(originId, destinationId, date):
    firstLeg = getTrip(originId, destinationId, date, "10:00")
    secondLeg = getTrip(destinationId, originId, date, "17:00")
    if firstLeg is None or secondLeg is None:
        return None
    price = firstLeg['price'] + secondLeg['price']
    return {"price": price, "firstLeg": firstLeg, "secondLeg": secondLeg}
