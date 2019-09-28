import requests


def getSBBToken():
    url = 'https://sso-INT.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token'
    data = {"grant_type": "client_credentials", "client_id": "22ebc2be",
            "client_secret": "2c820784f3e28837959abc43120989ca"}
    try:
        result = requests.post(url, data=data)
        return result.json()
    except Exception as e:
        print(e)


def getTrip(originId, destinationId, date, time):
    token = getSBBToken()['access_token']
    url = 'https://b2p.app.sbb.ch/api/trips'
    headers = {"Authorization": f'{token}', "X-Contract-Id": "HAC222P",
               "X-Conversation-Id": "cafebabe-0815-4711-1234-ffffdeadbeef"}
    params = {"originId": originId, "destinationId": destinationId,
              "date": date, "time": time}
    try:
        res = requests.get(url, headers=headers, params=params)
        return res.json()
    except Exception as e:
        print(e)
